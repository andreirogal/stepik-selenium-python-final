# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose a language e.g. ru, es, fr, en etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language:
        options = Options()
        options.add_experimental_option("prefs", {
            "intl.accept_languages": user_language})
        print(f"\nstart browser for test use language='{user_language}'...")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError(
            "--language should be e.g. ru, es, fr, en etc.")
    yield browser
    print("\nquit browser")
    browser.quit()
