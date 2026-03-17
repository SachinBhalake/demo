import pytest
from Page.homepage import HomePage
from Utilities.get_test_data import get_test_data

data = get_test_data("TestData/ui_test_data.yaml")

class TestHomepage:

    @pytest.mark.ui
    def test_01_homepage_logo(self, driver, logger):
        logger.info("Test Started: Verify homepage logo")
        hp = HomePage(driver, logger)
        assert hp.is_logo_visible(), "Test Failed: Logo is missing."
        logger.info("Test Passed: Logo is visible")

    @pytest.mark.ui
    def test_02_homepage_title(self, driver, logger):
        logger.info("Test Started: Verify homepage title")
        hp = HomePage(driver, logger)
        assert hp.get_homepage_title() == data["homepage"]["title"], "Test Failed: Homepage title mismatch"
        logger.info("Test Passed: Title matched")