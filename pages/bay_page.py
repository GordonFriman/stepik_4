from .locators import BayPageLocators

from .base_page import BasePage

text1 = ' был добавлен в вашу корзину.'
text2 = 'Стоимость корзины теперь составляет '


class BayPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*BayPageLocators.BASKET_BUTTON)
        basket_button.click()

    def shoulb_be_add_message(self):
        product_name = self.browser.find_element(*BayPageLocators.PRODUCT_NAME).text
        assert product_name == self.browser.find_element(
            *BayPageLocators.ADD_MESSAGE).text, 'Товар не добавлен в корзину'

    def should_be_basket_cost_message(self):
        product_cost = self.browser.find_element(*BayPageLocators.PRODUCT_COST).text
        assert product_cost in self.browser.find_element(
            *BayPageLocators.COST_MESSAGE).text, 'Не правильная стоимость корзины'
