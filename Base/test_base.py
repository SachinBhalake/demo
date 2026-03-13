
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_element(self, locator, element):
        if locator:
            element = self.get_element(*locator)
        element.click()

    def send_data(self, data, locator, element):
        if locator:
            element = self.get_element(*locator)
        element.clear()
        element.send_keys(data)

    def get_text(self, locator, element):
        if locator:
            element = self.get_element(*locator)
        text = element.text
        if len(text) == 0:
            text = element.get_attribute("innerText")
        if len(text) != 0:
            text = text.strip()
        return text