# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    MSG_PRODUCT_ADDED = (
        By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alert-info p strong")
