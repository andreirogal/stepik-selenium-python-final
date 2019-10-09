# -*- coding: utf-8 -*-

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_product_name_and_product_added_to_basket()
    page.should_be_equal_product_price_and_basket_value()
