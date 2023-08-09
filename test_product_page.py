import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        login_page.open()
        email = f"test_user_{time.time()}@fakemail.org"
        password = "test123456789"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
        page.open()
        page.should_be_item_add_to_basket()
        page.should_be_name_match()
        page.should_be_price_match()



# initial_url = ProductPageLocators.PRODUCT_URL
# urls = [f"{initial_url}/?promo=offer{i}" for i in range(10)]

@pytest.mark.need_review
# @pytest.mark.parametrize('link', urls)   ----- Убрал для упрощения проверки
# @pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
    product_page.open()
    product_page.should_be_item_add_to_basket()
    product_page.should_be_name_match()
    product_page.should_be_price_match()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL, 0)
    page.open()
    page.should_be_item_add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL, 0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL, 0)
    page.open()
    page.should_be_item_add_to_basket()
    page.should_disappear_element()

def test_guest_should_see_login_link_on_product_page(browser):
    page = BasketPage(browser, ProductPageLocators.PRODUCT_URL2)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasketPage(browser, ProductPageLocators.PRODUCT_URL2)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, ProductPageLocators.PRODUCT_URL)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_text_empty_basket()

