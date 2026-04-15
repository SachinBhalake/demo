from Page.pageobject import PageObject
from Utilities.get_test_data import get_test_data

test_data = get_test_data("../TestData/ui_test_data.yaml")

class Steps(PageObject):

    def verify_signup(self):
        self.logger.info(f"Verifying register new user and delete it")
        nav_result = self.navigate_to("signup")
        assert nav_result["status"] == "success", nav_result["message"]

        name = test_data["homepage"]["signup_name"]
        email = test_data["homepage"]["signup_email"]
        password = test_data["homepage"]["signup_password"]
        title = test_data["homepage"]["signup_title"]
        day = test_data["homepage"]["signup_day"]
        month = test_data["homepage"]["signup_month"]
        year = test_data["homepage"]["signup_year"]
        news = test_data["homepage"]["signup_news"]
        offer = test_data["homepage"]["signup_offer"]
        firstname = test_data["homepage"]["signup_firstname"]
        lastname = test_data["homepage"]["signup_lastname"]
        company = test_data["homepage"]["signup_company"]
        address1 = test_data["homepage"]["signup_address1"]
        address2 = test_data["homepage"]["signup_address2"]
        country = test_data["homepage"]["signup_country"]
        state = test_data["homepage"]["signup_state"]
        city = test_data["homepage"]["signup_city"]
        zipcode = test_data["homepage"]["signup_zipcode"]
        mobile = test_data["homepage"]["signup_mobile"]

        signup_result = self.signup(name, email, password, title, day, month, year,
               news, offer, firstname, lastname, company, address1,
               address2, country, state, city, zipcode, mobile)
        assert signup_result["status"] == "success", signup_result["message"]

        delete_result = self.delete_account()
        assert delete_result["status"] == "success", delete_result["message"]

    def verify_login(self):
        self.logger.info(f"Verifying login user and logout")

        nav_result = self.navigate_to("login")
        assert nav_result["status"] == "success", nav_result["message"]

        username = test_data["homepage"]["login_username"]
        password = test_data["homepage"]["login_password"]
        login_result = self.login(username, password)
        assert login_result["status"] == "success", login_result["message"]

        logout_result = self.logout()
        assert logout_result["status"] == "success", logout_result["message"]

    def verify_contact_us(self):

        self.logger.info(f"Verifying contact us")

        nav_result = self.navigate_to("contactus")
        assert nav_result["status"] == "success", nav_result["message"]

        name = test_data["homepage"]["contact_us_name"]
        email = test_data["homepage"]["contact_us_email"]
        subject = test_data["homepage"]["contact_us_subject"]
        message = test_data["homepage"]["contact_us_message"]
        file = test_data["homepage"]["contact_us_file"]

        contactus_result = self.contact_us(name, email, subject, message, file)
        assert contactus_result["status"] == "success", contactus_result["message"]

    def verify_search_product(self):

        self.logger.info(f"Verifying search product")

        nav_result = self.navigate_to("products")
        assert nav_result["status"] == "success", nav_result["message"]

        product_name = test_data["homepage"]["product_name"]
        search_result = self.search_product(product_name)
        assert search_result["status"] == "success", search_result["message"]

    def verify_cart_details(self):
        self.logger.info(f"Verifying cart details")

        nav_result = self.navigate_to("products")
        assert nav_result["status"] == "success", nav_result["message"]

        product_name = test_data["homepage"]["product_name"]
        product_quantity = test_data["homepage"]["product_quantity"]
        product_category = test_data["homepage"]["product_category"]
        product_price = test_data["homepage"]["product_price"]

        search_result = self.search_product(product_name)
        assert search_result["status"] == "success", search_result["message"]

        view_result = self.view_product(product_name)
        assert view_result["status"] == "success", view_result["message"]

        add_result = self.add_product_to_cart(product_name, product_quantity)
        assert add_result["status"] == "success", add_result["message"]

        nav_result = self.navigate_to("cart")
        assert nav_result["status"] == "success", nav_result["message"]

        cart_result = self.cart_details(product_name, product_category, product_price, product_quantity)
        assert cart_result["status"] == "success", cart_result["message"]

        remove_result = self.remove_product_from_cart()
        assert remove_result["status"] == "success", remove_result["message"]

    def verify_place_order(self):
        pass



    def verify_product_filters(self):

        self.logger.info(f"Verifying product filters")

        nav_result = self.navigate_to("products")
        assert nav_result["status"] == "success", nav_result["message"]

        product_category = test_data["homepage"]["product_category"]
        product_subcategory = test_data["homepage"]["product_subcategory"]
        category_result = self.product_category_filter(product_category, product_subcategory)
        assert category_result["status"] == "success", category_result["message"]

        product_brand = test_data["homepage"]["product_brand"]
        brand_result = self.product_brand_filter(product_brand)
        assert brand_result["status"] == "success", brand_result["message"]


    def verify_navigations(self):
        self.logger.info(f"Verifying page navigations")

        nav_result = self.navigate_to("home")
        assert nav_result["status"] == "success" and "automationexercise" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("products")
        assert nav_result["status"] == "success" and "products" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("cart")
        assert nav_result["status"] == "success" and "view_cart" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("login")
        assert nav_result["status"] == "success" and "login" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("signup")
        assert nav_result["status"] == "success" and "login" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("testcases")
        assert nav_result["status"] == "success" and "test_cases" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("apitesting")
        assert nav_result["status"] == "success" and "api_list" in nav_result["message"], nav_result["message"]

        nav_result = self.navigate_to("contactus")
        assert nav_result["status"] == "success" and "contact_us" in nav_result["message"], nav_result["message"]
