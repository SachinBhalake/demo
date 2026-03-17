from selenium.webdriver.common.by import By
from Base.test_base import BasePage

class HomePage(BasePage):
    _logo = (By.XPATH, "//img[contains(@src,'/logo.png')]")
    _products = (By.XPATH, "//a[@href='/products']")

    def go_to_products(self):
        self.click(self._products)

    def is_logo_visible(self):
        return self.get_element(self._logo).is_displayed()

    def get_homepage_title(self):
        return self.get_title()
