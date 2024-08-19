import time
import pytest
from pages.registration_page import RegistrationPage
import config
from selenium.webdriver.common.by import By
from pages.locators import RegistrationPageLocators
from support.email_utils import generate_temporary_email, get_confirmation_link


@pytest.fixture(scope="module")
def temp_email(request):
    email = request.config.cache.get("email_cache", None)
    return email


def test_register_with_valid_data(browser, request):
    email, api_url = generate_temporary_email()

    link = 'https://dev.abra-market.com/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
    page.enter_email(email)
    page.enter_password(config.valid_reg_password)
    page.submit_create_account_button()
    assert browser.find_element(By.XPATH, '//div[text()="A link for sign up has been sent to your email address."]')
    assert browser.current_url == 'https://dev.abra-market.com/register/check_email'

    confirmation_link = get_confirmation_link(email, api_url)
    browser.get(confirmation_link)
    print(f'Confirmation link: {confirmation_link}')

    assert "confirm_email" in browser.current_url
    page.complete_user_registration()
    time.sleep(2)

    request.config.cache.set("email_cache", email)


def test_registration_with_existing_email(browser, temp_email):
    email = temp_email
    print(f"[INFO] Using email in test: {email}")

    link = 'https://dev.abra-market.com/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
    page.enter_email(email)
    page.enter_password(config.valid_reg_password)
    page.submit_create_account_button()
    assert browser.find_element(By.CSS_SELECTOR, 'p.NoticePopup_message__Thz3M')


@pytest.mark.parametrize('email', config.invalid_reg_emails)
def test_registration_with_invalid_email(browser, email):
    link = 'https://dev.abra-market.com/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
    page.enter_email(email)
    page.enter_password(config.valid_reg_password)
    button = browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    assert button.get_attribute('disabled')
    assert browser.find_element(By.CLASS_NAME, 'Input_error__GM1PP')


@pytest.mark.parametrize('password', config.invalid_reg_passwords)
def test_registration_with_invalid_password(browser, password):
    link = 'https://dev.abra-market.com/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.select_role_supplier()
    page.enter_email('valid-email@gmail.com')
    page.enter_password(password)
    button = browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    assert button.get_attribute('disabled')
    # assert browser.find_element(By.CLASS_NAME, 'Input_error__GM1PP')
