import time
import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i=='bugged_link', reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    time.sleep(10)
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.check_cart()
