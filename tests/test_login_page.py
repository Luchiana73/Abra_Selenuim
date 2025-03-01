import pytest
from pages.login_page import LoginPage
import settings
import test_data
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators


@pytest.mark.parametrize('email', [settings.SUPPLIER_EMAIL, settings.SELLER_EMAIL])
def test_correct_login(browser, email):
    link = 'https://dev.abra-market.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(email)
    page.enter_password(settings.PASSWORD)
    page.submit_login_button()
    if email == settings.SUPPLIER_EMAIL:
        assert browser.find_element(By.CLASS_NAME, 'SupplierTop_supplier_link__zqbw3')
    else:
        assert browser.find_element(By.CSS_SELECTOR, 'button.HeaderCategories_button__Lv0HF')


@pytest.mark.parametrize('email', test_data.invalid_login_emails)
def test_login_fails_with_invalid_email(browser, email):
    link = 'https://dev.abra-market.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(email)
    page.enter_password(settings.PASSWORD)
    page.submit_login_button()
    assert browser.current_url == link, "User was able to log in using an invalid email"
    assert browser.find_element(*LoginPageLocators.LOGIN_EMAIL), \
        "Login form is not present, user logged in with an invalid email"


@pytest.mark.parametrize('password', test_data.invalid_login_passwords)
def test_supplier_login_fails_with_invalid_password(browser, password):
    link = 'https://dev.abra-market.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(settings.SUPPLIER_EMAIL)
    page.enter_password(password)
    page.submit_login_button()
    assert browser.current_url == link, "User was able to log in using an invalid password"
    assert browser.find_element(*LoginPageLocators.LOGIN_PASS), \
        "Login form is not present, user logged in with an invalid password"


@pytest.mark.parametrize('password', test_data.invalid_login_passwords)
def test_seller_login_fails_with_invalid_password(browser, password):
    link = 'https://dev.abra-market.com/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email(settings.SELLER_EMAIL)
    page.enter_password(password)
    page.submit_login_button()
    assert browser.current_url == link, "User was able to log in using an invalid password"
    assert browser.find_element(*LoginPageLocators.LOGIN_PASS), \
        "Login form is not present, user logged in with an invalid password"
