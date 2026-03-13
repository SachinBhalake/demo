from Page.homepage import HomePage


class Test_TC001_Homepage:

    def test_verify_Logo(self, driver):
        hp = HomePage(driver)
        assert hp.verify_logo()
