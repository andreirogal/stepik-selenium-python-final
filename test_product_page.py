# -*- coding: utf-8 -*-

import pytest

from pages.basket_page import BasketPage
from pages.dropmail_page import DropMailPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        dropmail_page = DropMailPage(browser, url="https://dropmail.me")
        dropmail_page.open()
        user_email = dropmail_page.get_email_from_dropmail()

        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, url=browser.current_url)
        login_page.register_new_user(user_email, user_email)
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/" \
               "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_equal_product_name_and_product_added_to_basket()
        page.should_be_equal_product_price_and_basket_value()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/" \
               "coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_basket()
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
