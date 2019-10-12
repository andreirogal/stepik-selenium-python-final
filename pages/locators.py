# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MSG_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")


class DropMailLocators:
    EMAIL = (By.CSS_SELECTOR, ".email")


class MainPageLocators:
    pass


class LoginPageLocators:
    BTN_REG_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CONFIRM_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    MSG_PRODUCT_ADDED = (
        By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alert-info p strong")
