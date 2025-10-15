﻿import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
