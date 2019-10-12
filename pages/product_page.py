# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def should_be_equal_product_name_and_product_added_to_basket(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(
                   *ProductPageLocators.MSG_PRODUCT_ADDED).text, "Names " \
                                                                 "do not match"

    def should_be_equal_product_price_and_basket_value(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(
                   *ProductPageLocators.BASKET_VALUE).text, "Prices " \
                                                            "do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MSG_PRODUCT_ADDED), \
            "Success message that product is added is presented, " \
            "but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.MSG_PRODUCT_ADDED), \
            "Success message that product is added is disappeared"
