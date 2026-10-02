from page.base_page import BasePage
from page.locators import MainPageLocators, ProductPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.is_element_present(*MainPageLocators.EMPTY_BASKET_MESSAGE,error_message="Ожидалось сообщение о пустой корзине")
        self.is_element_not_present(*ProductPageLocators.PRODUCT_NAME,error_message="Не ожидались товары в корзине")
