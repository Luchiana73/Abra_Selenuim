import time
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.setup_account_page import SetupPersonalAccountPage, SetupBusinessAccountPage
import config
from config import base_url
from selenium.webdriver.common.by import By
from pages.locators import RegistrationPageLocators
from support.email_utils import generate_temporary_email, get_confirmation_link
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_and_setup_supplier_account_flow(browser, user_cleanup):
    email, api_url = generate_temporary_email()

    # User registration
    reg_page_link = f'{base_url}register'
    registration_page = RegistrationPage(browser, reg_page_link)
    registration_page.open()
    registration_page.select_role_supplier()
    registration_page.enter_email(email)
    registration_page.enter_password(config.valid_reg_password)
    registration_page.submit_create_account_button()
    assert browser.find_element(*RegistrationPageLocators.LINK_SENT_MESSAGE)
    assert browser.current_url == f'{base_url}register/check_email'

    # Registration confirmation
    confirmation_link = get_confirmation_link(email, api_url)
    browser.get(confirmation_link)
    print(f'Confirmation link: {confirmation_link}')

    assert "confirm_email" in browser.current_url
    registration_page.complete_user_registration()

    # Clearing all cookies
    browser.delete_all_cookies()

    # Login
    login_page_link = f'{base_url}login'
    login_page = LoginPage(browser, login_page_link)
    login_page.open()
    login_page.enter_email(email)
    login_page.enter_password(config.valid_reg_password)
    login_page.submit_login_button()
    WebDriverWait(browser, 10).until(EC.url_contains("account_setup_personal_info"))
    assert browser.find_element(By.CLASS_NAME, 'SupplierRegisterFormStep_title__9g20k')

    # Account setup (personal information)
    setup_personal_page_link = f'{base_url}account_setup_personal_info'
    setup_page = SetupPersonalAccountPage(browser, setup_personal_page_link)
    setup_page.open()
    setup_page.enter_first_name()
    setup_page.enter_last_name()
    setup_page.select_phone_number_country()
    setup_page.enter_phone_number()
    setup_page.submit_continue_button()
    WebDriverWait(browser, 10).until(EC.url_contains("account_setup_business_info"))

    # Account setup (business information)
    setup_business_page_link = f'{base_url}account_setup_business_info'
    setup_page = SetupBusinessAccountPage(browser, setup_business_page_link)
    setup_page.open()
    # setup_page.upload_profile_logo()
    setup_page.enter_shop_name()
    setup_page.select_business_sector()
    setup_page.select_manufacturer_option()
    setup_page.fill_license_number()
    setup_page.enter_year_established()
    setup_page.select_number_of_employees()
    setup_page.select_country_of_company_registration()
    setup_page.fill_business_description()
    time.sleep(2)
    setup_page.select_business_phone_number_country()
    setup_page.enter_business_phone_number()
    setup_page.enter_business_email_address()
    setup_page.enter_company_address()
    # setup_page.submit_save_profile_button()
    assert WebDriverWait(browser, 10).until(
        EC.url_to_be(base_url)), f"Expected URL to be {base_url}, but got {browser.current_url}."

    # Delete user at the end of test
    # user_cleanup(base_url, email)
