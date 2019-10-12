# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import DropMailLocators


class DropMailPage(BasePage):
    def get_email_from_dropmail(self):
        self.browser.get("https://dropmail.me")
        return self.browser.find_element(*DropMailLocators.EMAIL).text
