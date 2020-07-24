import pytest

from .pages.bay_page import BayPage
import time


@pytest.mark.parametrize('step',
                         ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, step):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{step}'
    page = BayPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.shoulb_be_add_message()
    page.should_be_basket_cost_message()
    # time.sleep(100)