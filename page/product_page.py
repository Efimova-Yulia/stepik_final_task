from itertools import product

from page.base_page import BasePage
from page.locators import ProductPageLocators


class ProductPage(BasePage):

    #добавление товара в корзину
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
    #проверка сообщения об успешном добавлении в корзину
    def should_be_add_to_basket(self):
        self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение о добавлении в корзину не отображается'
    #проверка корректности названия товара в сообщении
    def should_be_correct_product_name_in_message(self ):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message_name, f'Несоответствие: название товара {product_name} в сообщении об успешном добавлении {message_name}'
    #проверка наличия стоимости корзины
    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE),'Стоимость корзины не отображается'
    #проверка корректности стоимости корзины с ценой товара
    def should_be_correct_basket_total(self):
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_message=self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == total_message, f'Несоответствие: цена товара {product_price}, стоимость корзины {total_message}'



