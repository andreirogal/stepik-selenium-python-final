# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_msg_that_basket_is_empty(self):
        assert "basket is empty" in \
               self.browser.find_element(
                   *BasketPageLocators.MSG_BASKET_IS_EMPTY).text
