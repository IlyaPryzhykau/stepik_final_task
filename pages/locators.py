from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group > a')


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    INPUT_REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    INPUT_REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTER = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators():
    PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    PRODUCT_URL2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_ADDNAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ITEM_ADDPRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, '#basket_totals')
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')

