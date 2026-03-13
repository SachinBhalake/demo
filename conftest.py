import os
import pytest
import pytest_html
from Utilities.webdriver import get_driver
from Utilities.getconfig import ConfigReader


def pytest_addoption(parser):

    parser.addoption("--browser", action="store")
    parser.addoption("--env", action="store")


@pytest.fixture
def driver(request):

    config = ConfigReader()

    browser = request.config.getoption("--browser") or config.get_browser()
    env = request.config.getoption("--env") or config.config["env"]
    url = config.get_base_url(env)

    if browser is None:
        browser = config.get_browser()

    print("====>>>>", browser, url)

    driver = get_driver(browser)

    driver.get(url)

    yield driver

    driver.quit()


@pytest.fixture
def base_url(request):

    config = ConfigReader()

    env = request.config.getoption("--env")

    if env is None:
        env = config.config["env"]

    return config.config["environments"][env]["base_url"]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            session_id = driver.session_id

            video_path = f"videos/{session_id}.mp4"

            if os.path.exists(video_path):

                extras = getattr(report, "extras", [])

                extras.append(
                    pytest_html.extras.html(
                        f"""
                        <video width="400" controls>
                            <source src="../{video_path}" type="video/mp4">
                        </video>
                        """
                    )
                )

                report.extras = extras