from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
from .pages.locators import MainPageLocators
from .pages.basket_page import BasketPage
import time

def test_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_should_be_login_page(browser):
    login_page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
    login_page.open()
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_LINK)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_text_empty_basket()

