import os
import time
import allure
from datetime import datetime
import pytest
import pytest_html
from Utilities.webdriver import get_driver
from Utilities.get_config import ConfigReader
from Utilities.helper import wait_for_video_complete
from Utilities.logger import get_logger

@pytest.fixture
def logger(request):
    test_name = request.node.name
    logger, log_file = get_logger(test_name)

    request.node.log_file = log_file
    return logger

def pytest_addoption(parser):

    parser.addoption("--browser", action="store")
    parser.addoption("--env", action="store")

@pytest.fixture
def driver(request):

    config = ConfigReader()

    browser = request.config.getoption("--browser") or config.get_browser()
    env = request.config.getoption("--env") or config.config["env"]
    url = config.get_base_url(env)

    driver = get_driver(browser)

    driver.get(url)

    yield driver

    driver.quit()


@pytest.fixture
def base_url(request):

    config = ConfigReader()

    env = request.config.getoption("--env") or config.config["env"]

    return config.config["environments"][env]["base_url"]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return

    if report.failed:
        driver = item.funcargs.get("driver")
        if not driver:
            return
        if driver:

            extras = getattr(report, "extras", [])
            if extras is None:
                extras = []

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_dir = "Reports/Screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_full_path = os.path.join(screenshot_dir, screenshot_name)
            driver.save_screenshot(screenshot_full_path)
            screenshot_rel_path = f"../Screenshots/{screenshot_name}"
            if os.path.exists(screenshot_full_path):
                allure.attach.file(
                    screenshot_full_path,
                    name="Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            session_id = driver.session_id
            video_full_path = f"Reports/Videos/{session_id}.mp4"

            # Wait until file appears
            if not os.path.exists(video_full_path):
                for _ in range(15):
                    if os.path.exists(video_full_path):
                        break
                    time.sleep(1)

            # Wait until video writing is complete
            if os.path.exists(video_full_path) and wait_for_video_complete(video_full_path):
                video_rel_path = f"../Videos/{session_id}.mp4"

                combined_html = f"""
                <div style="padding:10px;">
                    <div>
                        <b>Screenshot:</b><br>
                        <img src="{screenshot_rel_path}" width="400"/>
                    </div>

                    <div style="margin-top:10px;">
                        <a href="{video_rel_path}" target="_blank" style="font-weight:bold; color:blue;">
                            ▶️ View Execution Video
                        </a>
                    </div>
                </div>
                """

                extras.append(pytest_html.extras.html(combined_html))
                report.extras = extras

                allure.attach.file(
                    video_full_path,
                    name="Video",
                    attachment_type=allure.attachment_type.MP4
                )