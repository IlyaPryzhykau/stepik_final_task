import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

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
