import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
import test_data
from pages.locators import RegistrationPageLocators


def test_register_with_valid_data(browser, generated_email):
    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_seller()
    page.enter_email(generated_email)
    page.enter_password(test_data.valid_reg_password)
    page.submit_create_account_button()
    print(generated_email)
    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        RegistrationPageLocators.SUCCESS_MESSAGE))
    assert browser.current_url == f'{test_data.base_url}register/check_email'


def test_registration_with_existing_email_flow(browser, generated_email):
    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)

    # 1. First registration
    page.open()
    page.select_role_seller()
    page.enter_email(generated_email)
    page.enter_password(test_data.valid_reg_password)
    page.submit_create_account_button()
    print(generated_email)
    # wait for the backend to complete the registration
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        RegistrationPageLocators.SUCCESS_MESSAGE))

    # 2. Second registration attempt
    page.open()
    page.select_role_seller()
    page.enter_email(generated_email)
    page.enter_password(test_data.valid_reg_password)
    time.sleep(1)  # necessary for stability
    page.submit_create_account_button()
    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        RegistrationPageLocators.EXISTING_EMAIL_ERROR)), \
        "Error message 'Email is already registered' was not shown"


@pytest.mark.parametrize('email', test_data.invalid_reg_emails)
def test_registration_with_invalid_email(browser, email):
    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_seller()
    page.enter_email(email)
    page.enter_password(test_data.valid_reg_password)
    page.submit_create_account_button()
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_ERROR)
    )


@pytest.mark.parametrize('password', test_data.invalid_reg_passwords)
def test_registration_with_invalid_password(browser, password):
    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_seller()
    page.enter_email('valid-email@gmail.com')
    page.enter_password(password)
    page.submit_create_account_button()
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_ERROR)
    )
