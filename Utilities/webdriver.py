from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Utilities.get_config import ConfigReader


def get_driver(browser):

    config = ConfigReader()
    grid_url = config.get_grid_url()

    browser = browser.lower()

    if browser == "chrome":
        options = ChromeOptions()

    elif browser == "firefox":
        options = FirefoxOptions()

    else:
        raise ValueError("Browser must be chrome or firefox")

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )

    driver.maximize_window()

    return driver