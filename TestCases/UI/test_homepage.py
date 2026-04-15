import pytest
from Page.steps import Steps


@pytest.mark.ui
class TestPageObject:

    def test_01_verify_valid_signup(self, driver, logger):
        logger.info("Test Started: Verify valid signup")
        s = Steps(driver, logger)
        s.verify_signup()

    def test_02_verify_invalid_signup(self, driver, logger):
        logger.info("Test Started: Verify invalid signup")
        s = Steps(driver, logger)
        s.verify_signup()

    def test_03_verify_valid_login(self, driver, logger):
        logger.info("Test Started: Verify valid login")
        s = Steps(driver, logger)
        s.verify_login()

    def test_04_verify_invalid_login(self, driver, logger):
        logger.info("Test Started: Verify invalid login")
        s = Steps(driver, logger)
        s.verify_login()

    def test_05_verify_contact_us(self, driver, logger):
        logger.info("Test Started: Verify contact us")
        s = Steps(driver, logger)
        s.verify_contact_us()

    def test_06_verify_search_product(self, driver, logger):
        logger.info("Test Started: Verify search product")
        s = Steps(driver, logger)
        s.verify_search_product()

    def test_07_verify_cart_details(self, driver, logger):
        logger.info("Test Started: Verify cart details")
        s = Steps(driver, logger)
        s.verify_cart_details()

    def test_08_verify_place_order(self, driver, logger):
        logger.info("Test Started: Verify place order")
        s = Steps(driver, logger)
        s.verify_place_order()

    def test_09_verify_product_filters(self, driver, logger):
        logger.info("Test Started: Verify product filters")
        s = Steps(driver, logger)
        s.verify_product_filters()

    def test_10_verify_navigations(self, driver, logger):
        logger.info("Test Started: Verify navigations")
        s = Steps(driver, logger)
        s.verify_navigations()
