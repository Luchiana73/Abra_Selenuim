import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Ui_Tests.pages.base_page import BasePage
from Ui_Tests.pages.locators import SetupAccountPageLocators
from config import generate_turkey_phone_number, generate_licence_number, generate_year, generate_turkish_address
from faker import Faker

fake = Faker()


class SetupPersonalAccountPage(BasePage):
    def enter_first_name(self):
        first_name = fake.first_name()
        first_name_field = self.browser.find_element(*SetupAccountPageLocators.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)
        print(f"First name: {first_name}")

    def enter_last_name(self):
        last_name = fake.last_name()
        first_name_field = self.browser.find_element(*SetupAccountPageLocators.LAST_NAME_FIELD)
        first_name_field.send_keys(last_name)
        print(f"Last name: {last_name}")

    def select_phone_number_country(self):
        self.browser.find_element(*SetupAccountPageLocators.PHONE_COUNTRY_DROPDOWN).click()
        self.browser.find_element(*SetupAccountPageLocators.COUNTRY_LOCATOR_TURKEY).click()

    def enter_phone_number(self):
        phone_number = generate_turkey_phone_number()
        phone_number_field = self.browser.find_element(*SetupAccountPageLocators.PHONE_NUMBER_FIELD)
        phone_number_field.send_keys(phone_number)

    def submit_continue_button(self):
        self.browser.find_element(*SetupAccountPageLocators.SUBMIT_FIRST_STEP_BUTTON).click()


class SetupBusinessAccountPage(BasePage):
    def upload_profile_logo(self):
        file_path = r'D:\Desktop\PycharmProjects\Abra_testing_on_Python\tests\images\logo_2.png'
        self.browser.find_element(*SetupAccountPageLocators.UPLOAD_LOGO_INPUT).send_keys(file_path)

    def enter_shop_name(self):
        shop_name = fake.company()
        first_name_field = self.browser.find_element(*SetupAccountPageLocators.SHOP_NAME_FIELD)
        first_name_field.send_keys(shop_name)
        print(f"Shop name: {shop_name}")

    def select_business_sector(self):
        self.browser.find_element(*SetupAccountPageLocators.SELECT_BUSINESS_SECTOR_DROPDOWN).click()
        self.browser.find_element(*SetupAccountPageLocators.CLOTHES_BUSINESS_SECTOR).click()

    def select_manufacturer_option(self):
        self.browser.find_element(*SetupAccountPageLocators.MANUFACTURER_CHECKBOX).click()

    def fill_license_number(self):
        license_number = generate_licence_number()
        self.browser.find_element(*SetupAccountPageLocators.LICENCE_NUMBER_FIELD).send_keys(license_number)
        print(f"Licence number: {license_number}")

    def enter_year_established(self):
        year = generate_year(1980)
        self.browser.find_element(*SetupAccountPageLocators.ESTABLISHMENT_YEAR_FIELD).send_keys(year)
        print(f"Year company established: {year}")

    def select_number_of_employees(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.NUMBER_OF_EMPLOYEES_DROPDOWN))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            SetupAccountPageLocators.NUMBER_OF_EMPLOYEES_DROPDOWN)).click()
        random_key = random.choice(list(SetupAccountPageLocators.NUMBER_OF_EMPLOYEES.keys()))
        locator = SetupAccountPageLocators.NUMBER_OF_EMPLOYEES[random_key]
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).click()

    def select_country_of_company_registration(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.COUNTRY_OF_COMPANY_REGISTRATION_DROPDOWN))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            SetupAccountPageLocators.COUNTRY_OF_COMPANY_REGISTRATION_DROPDOWN)).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            SetupAccountPageLocators.COUNTRY_OF_COMPANY_REGISTRATION_TURKEY))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            SetupAccountPageLocators.COUNTRY_OF_COMPANY_REGISTRATION_TURKEY)).click()

    def fill_business_description(self):
        text = fake.paragraph(nb_sentences=3)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.BUSINESS_DESCRIPTION_FIELD)).send_keys(text)

    def select_business_phone_number_country(self):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.BUSINESS_PHONE_COUNTRY_DROPDOWN))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            SetupAccountPageLocators.BUSINESS_PHONE_COUNTRY_DROPDOWN)).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            SetupAccountPageLocators.BUSINESS_COUNTRY_LOCATOR_TURKEY))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            SetupAccountPageLocators.BUSINESS_COUNTRY_LOCATOR_TURKEY)).click()

    def enter_business_phone_number(self):
        phone_number = generate_turkey_phone_number()
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.PHONE_NUMBER_FIELD)).send_keys(phone_number)

    def enter_business_email_address(self):
        email = fake.email()
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.BUSINESS_EMAIL_FIELD)).send_keys(email)
        print(f"Company email: {email}")

    def enter_company_address(self):
        turkish_address = generate_turkish_address()
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
            SetupAccountPageLocators.COMPANY_ADDRESS_FIELD)).send_keys(turkish_address)
        print(f"Company address: {turkish_address}")

    def submit_save_profile_button(self):
        self.browser.find_element(*SetupAccountPageLocators.PROFILE_SAVE_BUTTON).click()
