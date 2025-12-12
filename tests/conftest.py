from dotenv import load_dotenv
load_dotenv()
import pytest
from selenium import webdriver
import settings
from pages.login_page import LoginPage
import time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def generated_email():
    return f"test_{int(time.time())}@gmail.com"

@pytest.fixture()
def login_supplier(browser):
    link = 'https://dev.marketabra.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(settings.SUPPLIER_EMAIL)
    page.enter_password(settings.PASSWORD)
    page.submit_login_button()
    return browser


@pytest.fixture()
def login_seller(browser):
    link = 'https://dev.marketabra.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(settings.SELLER_EMAIL)
    page.enter_password(settings.PASSWORD)
    page.submit_login_button()
    return browser
