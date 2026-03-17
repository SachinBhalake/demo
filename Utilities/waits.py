from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_page_load(self):
        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def all_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))