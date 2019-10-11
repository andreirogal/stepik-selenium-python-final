# -*- coding: utf-8 -*-

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize("link", [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        "?promo=offer7",
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    "?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_product_name_and_product_added_to_basket()
    page.should_be_equal_product_price_and_basket_value()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/" \
           "the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/" \
           "the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_btn_view_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items()
    basket_page.should_be_msg_that_basket_is_empty()
