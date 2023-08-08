from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert (self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL)), \
            "There is an item in basket"

    def should_be_text_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text
        assert 'Your basket is empty.' in text, "Empty basket text missing"

