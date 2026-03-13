from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_driver(browser):

    grid_url = "http://localhost:4444/wd/hub"

    if browser.lower() == "chrome":
        options = ChromeOptions()

    elif browser.lower() == "firefox":
        options = FirefoxOptions()

    else:
        raise ValueError("Browser must be chrome or firefox")

    driver = webdriver.Remote(command_executor=grid_url, options=options)
    #driver = webdriver.Chrome()

    driver.maximize_window()

    return driver