import pytest

from page.locators import ProductPageLocators
from page.main_page import MainPage
from page.product_page import ProductPage

# @pytest.mark.parametrize('promo_offer',["0","1", "3", "4", "5", "6",
#                                         pytest.param("7",marks=pytest.mark.xfail)
#     , "8", "9"])

# def test_guest_can_add_product_to_basket (browser,promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#
#     page = MainPage(browser, link)
#     product_page = ProductPage(browser, link)
#
#     page.open()
#     product_page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     product_page.should_be_add_to_basket()
#     product_page.should_be_correct_product_name_in_message()
#     product_page.should_be_basket_total_message()
#     product_page.should_be_correct_basket_total()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()






