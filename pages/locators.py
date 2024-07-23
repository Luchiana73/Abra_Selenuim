from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    LOGIN_PASS = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class RegistrationPageLocators:
    SELECT_ROLE_SUPPLIER_BUTTON = (By.XPATH, "//button[text()=\"I'm here to sell\"]")
    SELECT_ROLE_SELLER_BUTTON = (By.XPATH, "//button[text()=\"I'm here to buy\"]")
    REGISTER_EMAIL = LoginPageLocators.LOGIN_EMAIL
    REGISTER_PASS = LoginPageLocators.LOGIN_PASS
    REGISTER_BUTTON = LoginPageLocators.LOGIN_BUTTON

