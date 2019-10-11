# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import LoginPageLocators, DropMailLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASS_FIELD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.PASS_CONFIRM_FIELD).send_keys(
            password)
        self.browser.find_element(*LoginPageLocators.BTN_REG_SUBMIT).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Url login page is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login from is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"
