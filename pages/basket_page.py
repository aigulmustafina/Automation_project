from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_is_empty(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert 'Your basket is empty' in basket_empty.text, 'Корзина не пуста'