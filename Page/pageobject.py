from Base.test_base import BasePage
from Page.locators import Locators


class PageObject(BasePage):

    def navigate_to(self, page):
        self.logger.info(f"Navigating to page: {page}")
        page=page.lower()
        if page=="home":
            self.click(Locators._home_button)
        elif page == "products":
            self.click(Locators._products_button)
        elif page == "cart":
            self.click(Locators._cart_button)
        elif page == "login" or page == "signup":
            self.click(Locators._signup_login_button)
        elif page == "testcases":
            self.click(Locators._testcases_button)
        elif page == "apitesting":
            self.click(Locators._api_testing_button)
        elif page == "contactus":
            self.click(Locators._contact_us_button)
        else:
            return {"status": "failure", "message": f"Unsupported page: {page}"}
        self.wait_for_page_load()
        return {"status": "success", "message": self.get_title()}

    def signup(self, name, email, password, title, day, month, year,
               news, offer, firstname, lastname, company, address1,
               address2, country, state, city, zipcode, mobile):
        self.logger.info(f"Signing up")

        self.wait.visible(Locators._signup_header1)

        self.send_keys(Locators._signup_username, name)
        self.send_keys(Locators._signup_email, email)
        self.click(Locators._signup_button)

        if self.wait.visible(Locators._signup_error, 3):
            return {"status": "failure", "message": "Email Address already exist!"}

        self.wait_for_page_load()

        self.wait.visible(Locators._signup_header2)

        if title:
            if title=="Mr":
                self.click(Locators._signup_title1)
            elif title=="Mrs":
                self.click(Locators._signup_title2)
            else:
                return {"status": "failure", "message": f"Unsupported title: {title}"}

        self.send_keys(Locators._signup_password, password)

        if day:
            self.select_dropdown(Locators._signup_date, day)
        if month:
            self.select_dropdown(Locators._signup_month, month)
        if year:
            self.select_dropdown(Locators._signup_year, year)
        if news:
            self.click(Locators._signup_newsletter)
        if offer:
            self.click(Locators._signup_offer)

        self.send_keys(Locators._signup_firstname, firstname)
        self.send_keys(Locators._signup_lastname, lastname)

        if company:
            self.send_keys(Locators._signup_company, company)

        self.send_keys(Locators._signup_address1, address1)

        if address2:
            self.send_keys(Locators._signup_address2, address2)

        self.select_dropdown(Locators._signup_country, country)
        self.send_keys(Locators._signup_state, state)
        self.send_keys(Locators._signup_city, city)
        self.send_keys(Locators._signup_zip, zipcode)
        self.send_keys(Locators._signup_mobile, mobile)
        self.click(Locators._signup_create_account_button)
        self.wait_for_page_load()
        if self.wait.visible(Locators._signup_success):
            self.click(Locators._signup_continue_button)
            self.wait_for_page_load()
            return {"status": "success", "message": "Account created"}
        else:
            return {"status": "failure", "message": "Account creation failed"}

    def delete_account(self):
        self.logger.info(f"Deleting account")
        self.click(Locators._delete_account_button)
        if self.wait.visible(Locators._delete_account_success):
            self.click(Locators._delete_account_continue_button)
            return {"status": "success", "message": "Account deleted"}
        return {"status": "failure", "message": "Account delete failed"}

    def login(self, username, password):
        self.logger.info(f"Logging in")
        self.wait.visible(Locators._login_header)
        self.send_keys(Locators._login_username, username)
        self.send_keys(Locators._login_password, password)
        self.click(Locators._login_button)
        self.wait_for_page_load()
        if self.wait.visible(Locators._login_success):
            return {"status": "success", "message": "Login success"}
        elif self.wait.visible(Locators._login_error):
            return {"status": "failure", "message": "Email or password is incorrect"}
        return {"status": "failure", "message": "Login failed"}

    def logout(self):
        self.logger.info(f"Logging out")
        self.click(Locators._logout_button)
        if self.wait.invisible(Locators._login_success) and self.wait.invisible(Locators._logout_button) and self.wait.visible(Locators._signup_login_button):
            return {"status": "success", "message": "Logout success"}
        else:
            return {"status": "failure", "message": "Logout failed"}

    def contact_us(self, name, email, subject, message, file):
        self.logger.info(f"Contact us")
        self.wait.visible(Locators._contact_us_header)
        if name:
            self.send_keys(Locators._contact_us_name, name)
        self.send_keys(Locators._contact_us_email, email)
        if subject:
            self.send_keys(Locators._contact_us_subject, subject)
        if message:
            self.send_keys(Locators._contact_us_message, message)
        if file:
            self.send_keys(Locators._contact_us_file, file)
        self.click(Locators._contact_us_submit_button)
        if self.wait.visible(Locators._contact_us_success):
            return {"status": "success", "message": "Contact us success"}
        else:
            return {"status": "failure", "message": "Contact us failed"}

    def search_product(self, product_name):
        self.logger.info(f"Searching product")
        self.send_keys(Locators._search_product_box, product_name)
        self.click(Locators._search_product_button)
        self.wait.visible(Locators._search_product_results)
        if product_name in self.get_text(Locators._search_product_results_text):
            return {"status": "success", "message": "Search product success"}
        else:
            return {"status": "failure", "message": "Search product failed"}

    def view_product(self, product_name):
        self.logger.info(f"View product")
        self.click(Locators._view_product_button)
        self.wait_for_page_load()
        if product_name in self.get_text(Locators._view_product_name):
            return {"status": "success", "message": "Product view success"}
        else:
            return {"status": "failure", "message": "Product view failed"}

    def product_details(self, product_name, product_category, product_price, product_availability, product_condition, product_brand):
        self.logger.info(f"Verifying product details")
        name = self.get_text(Locators._view_product_name)
        category = self.get_text(Locators._view_product_category)
        price = self.get_text(Locators._view_product_price)
        available = self.get_text(Locators._view_product_availability)
        condition = self.get_text(Locators._view_product_condition)
        brand = self.get_text(Locators._view_product_brand)
        if (product_name == name and product_category == category and product_price == price
            and product_availability == available and product_condition == condition and product_brand == brand):
            return {"status": "success", "message": "Product details success"}
        else:
            return {"status": "failure", "message": "Product details failed"}

    def add_product_to_cart(self, product_name, product_quantity):
        self.logger.info(f"Add product to cart")
        self.send_keys(Locators._view_product_quantity, product_quantity)
        self.click(Locators._add_to_cart_button)
        if self.wait.visible(Locators._add_to_cart_success):
            self.click(Locators._continue_shopping_button)
            return {"status": "success", "message": "Add product to cart success"}
        else:
            return {"status": "failure", "message": "Add product to cart failed"}

    def cart_details(self, product_name, product_category, product_price, product_quantity):
        self.logger.info(f"Verifying cart details")
        name = self.get_text(Locators._cart_product_name)
        category = self.get_text(Locators._cart_product_category)
        price = self.get_text(Locators._cart_product_price)
        quantity = self.get_text(Locators._cart_product_quantity)
        if (product_name == name and product_category == category and product_price == price
            and product_quantity == quantity):
            return {"status": "success", "message": "Cart details success"}
        else:
            return {"status": "failure", "message": "Cart details failed"}

    def remove_product_from_cart(self):
        self.logger.info(f"Remove product from cart")
        self.click(Locators._cart_product_remove_button)
        if self.wait.visible(Locators._cart_product_remove_success):
            return {"status": "success", "message": "Product remove success"}
        else:
            return {"status": "failure", "message": "Product remove failed"}

    def checkout(self, order_comment, card_name, card_number, card_cvc, card_month, card_year):
        self.logger.info(f"Checkout")
        self.click(Locators._cart_proceed_checkout_button)
        self.wait_for_page_load()
        self.send_keys(Locators._place_order_message, order_comment)
        self.click(Locators._place_order_button)
        self.wait.visible(Locators._payment_header)
        self.send_keys(Locators._payment_card_name, card_name)
        self.send_keys(Locators._payment_card_number, card_number)
        self.send_keys(Locators._payment_cvc, card_cvc)
        self.send_keys(Locators._payment_expiry_month, card_month)
        self.send_keys(Locators._payment_expiry_year, card_year)
        self.click(Locators._pay_and_confirm_button)
        if self.wait.visible(Locators._order_success):
            return {"status": "success", "message": "Checkout success"}
        else:
            return {"status": "failure", "message": "Checkout failed"}

    def product_category_filter(self, product_category, product_subcategory):
        self.logger.info(f"Verifying product category filter")
        self.click(Locators.category_button(product_category))
        self.click(Locators.subcategory_button(product_category, product_subcategory))
        if self.wait.visible(Locators.category_filter_results_header(product_category, product_subcategory)):
            return {"status": "success", "message": "Product category filter success"}
        else:
            return {"status": "failure", "message": "Product category filter failed"}

    def product_brand_filter(self, product_brand):
        self.logger.info(f"Verifying product brand filter")
        self.click(Locators.brand_button(product_brand))
        if self.wait.visible(Locators.brand_filter_results_header(product_brand)):
            return {"status": "success", "message": "Product brand filter success"}
        else:
            return {"status": "failure", "message": "Product brand filter failed"}
