from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        self.should_be_product_url()
        self.should_be_item_add_to_basket()


    def should_be_product_url(self):
        assert "login" in self.browser.current_url, "word \"catalogue\" not in url"

    def should_be_item_add_to_basket(self):
         add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
         add_button.click()


    def should_be_name_match(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_addname = self.browser.find_element(*ProductPageLocators.ITEM_ADDNAME).text
        assert item_name == item_addname, "The names don't match"


    def should_be_price_match(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        item_addprice = self.browser.find_element(*ProductPageLocators.ITEM_ADDPRICE).text
        assert item_price == item_addprice, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_element(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still present, but should disappear"

