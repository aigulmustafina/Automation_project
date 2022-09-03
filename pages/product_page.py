from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_product_to_cart_btn()
        self.should_be_title_of_book()
        self.should_be_price_of_book()

    def add_product_to_cart(self):
        cart_btn = self.browser.find_element(*ProductPageLocators.CART_BTN)
        cart_btn.click()

    def check_cart(self):
        self.should_be_same_book_title()
        self.should_be_same_price()

    def should_be_add_product_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.CART_BTN), 'Add to cart button is not presented'

    def should_be_title_of_book(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_TITLE), 'Book title is not presented'

    def should_be_price_of_book(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), 'Book price is not presented'

    def should_be_same_book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_title_in_cart = self.browser.find_element(*ProductPageLocators.BOOK_IN_CART)
        assert book_title.text == book_title_in_cart.text

    def should_be_same_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART)
        assert price.text == price_in_cart.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG),\
            'Success message is presented, but not should be'

    def should_disapear_success_message(self):
        assert self.is_disapeared(*ProductPageLocators.SUCCESS_MSG),\
            'Success message is presented, but not should be'