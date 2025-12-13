from dotenv import load_dotenv
load_dotenv()
import pytest
from selenium import webdriver
from settings import BASE_URL, SUPPLIER_EMAIL, SELLER_EMAIL, PASSWORD
from pages.login_page import LoginPage
import time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def generated_email():
    return f"test_{int(time.time())}@gmail.com"

@pytest.fixture()
def login_supplier(browser):
    link = f'{BASE_URL}login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(SUPPLIER_EMAIL)
    page.enter_password(PASSWORD)
    page.submit_login_button()
    return browser


@pytest.fixture()
def login_seller(browser):
    link = f'{BASE_URL}login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(SELLER_EMAIL)
    page.enter_password(PASSWORD)
    page.submit_login_button()
    return browser
