import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
import test_data
from pages.locators import RegistrationPageLocators
from support.email_utils import create_mailtm_account, get_confirmation_link_mailtm


@pytest.fixture(scope="module")
def temp_email(request):
    email = request.config.cache.get("email_cache", None)
    return email


def test_register_with_valid_data(browser, request):
    email, token = create_mailtm_account()

    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
    page.enter_email(email)
    page.enter_password(test_data.valid_reg_password)
    page.submit_create_account_button()
    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
        RegistrationPageLocators.SUCCESS_MESSAGE))
    assert browser.current_url == f'{test_data.base_url}register/check_email'

    confirmation_link = get_confirmation_link_mailtm(token)
    browser.get(confirmation_link)
    print(f'Confirmation link: {confirmation_link}')

    assert "confirm_email" in browser.current_url
    page.complete_user_registration()

    request.config.cache.set("email_cache", email)


def test_registration_with_existing_email(browser, temp_email):
    email = temp_email
    print(f"[INFO] Using email in test: {email}")

    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
    page.enter_email(email)
    page.enter_password(test_data.valid_reg_password)
    page.submit_create_account_button()
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.EXISTING_EMAIL_ERROR)
    ), "Error message 'Email is already registered' was not shown"


@pytest.mark.parametrize('email', test_data.invalid_reg_emails)
def test_registration_with_invalid_email(browser, email):
    link = f'{test_data.base_url}register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
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
    page.select_role_supplier()
    page.enter_email('valid-email@gmail.com')
    page.enter_password(password)
    page.submit_create_account_button()
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_ERROR)
    )

