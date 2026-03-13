from selenium.webdriver.common.by import By
from Base.test_base import BasePage

class HomePage(BasePage):
    _logo = (By.XPATH, "//img[contains(@src,'/logo.png')]")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_logo(self):
        elem = self.get_element(self._logo)
        return elem
