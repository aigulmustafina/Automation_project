from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_PAGE = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REG = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REG = (By.CSS_SELECTOR, '#register_form > button')
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_LOGIN = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_form > button')



class ProductPageLocators():
    CART_BTN = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BOOK_TITLE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    BOOK_IN_CART = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE_IN_CART = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCESS_MSG = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a > i')


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')

