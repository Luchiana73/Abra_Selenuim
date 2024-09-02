import requests

from Ui_Tests.pages.base_page import BasePage
from Ui_Tests.pages.locators import RegistrationPageLocators, ConfirmEmailPageLocators


class RegistrationPage(BasePage):
    def select_role_supplier(self):
        self.browser.find_element(*RegistrationPageLocators.SELECT_ROLE_SUPPLIER_BUTTON).click()

    def select_role_seller(self):
        self.browser.find_element(*RegistrationPageLocators.SELECT_ROLE_SELLER_BUTTON).click()

    def enter_email(self, email):
        reg_email = self.browser.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)

    def enter_password(self, password):
        reg_pass = self.browser.find_element(*RegistrationPageLocators.REGISTER_PASS)
        reg_pass.send_keys(password)

    def submit_create_account_button(self):
        reg_button = self.browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        reg_button.submit()

    def complete_user_registration(self):
        self.browser.find_element(*ConfirmEmailPageLocators.LOGIN_LINK).click()


def delete_user(base_url, email):
    delete_endpoint = f"{base_url}/users/account/delete"

    response = requests.delete(delete_endpoint, json={"email": email})

    if response.status_code == 200:
        print(f"User with email {email} has been deleted successfully.")
    else:
        print(f"Failed to delete user with email {email}. Status code: {response.status_code}")
        print(response.text)
