from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_ADDNAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ITEM_ADDPRICE = (By.CSS_SELECTOR, '.alertinner p strong')






