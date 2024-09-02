import pytest
from selenium import webdriver
import settings
from pages.login_page import LoginPage


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def login_supplier(browser):
    link = 'https://dev.abra-market.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(settings.SUPPLIER_EMAIL)
    page.enter_password(settings.PASSWORD)
    page.submit_login_button()
    return browser


@pytest.fixture()
def login_seller(browser):
    link = 'https://dev.abra-market.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(settings.SELLER_EMAIL)
    page.enter_password(settings.PASSWORD)
    page.submit_login_button()
    return browser
