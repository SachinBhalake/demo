from selenium import webdriver


def get_driver(browser, headless=False, grid=False, grid_url=None):

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        if grid:
            return webdriver.Remote(
                command_executor=grid_url,
                options=options
            )

        return webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        if grid:
            return webdriver.Remote(
                command_executor=grid_url,
                options=options
            )

        return webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")