import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

initial_url = ProductPageLocators.PRODUCT_URL
urls = [f"{initial_url}/?promo=offer{i}" for i in range(10)]


@pytest.mark.parametrize('link', urls)
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_item_add_to_basket()
    product_page.solve_quiz_and_get_code()
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
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()



