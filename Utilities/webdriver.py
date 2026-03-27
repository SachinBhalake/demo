from selenium import webdriver


def get_driver(browser, headless=False, grid=False, grid_url=None):

    browser = browser.lower()

    # -------------------------
    # CHROME
    # -------------------------
    if browser == "chrome":
        options = webdriver.ChromeOptions()

        # 🔥 CI Stability
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        # ✅ Headless only if needed
        if headless:
            options.add_argument("--headless=new")

        if grid:
            return webdriver.Remote(
                command_executor=grid_url,
                options=options
            )

        return webdriver.Chrome(options=options)

    # -------------------------
    # FIREFOX
    # -------------------------
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        # Firefox doesn't need all Chrome flags
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