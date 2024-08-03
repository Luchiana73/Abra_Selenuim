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


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/a[2]')
    REGISTRATION_LINK = (By.CSS_SELECTOR, 'a.Button_light_red__G4Gow[href="/register"]')
    All_CATEGORIES_LINK = (By.CSS_SELECTOR, 'button.HeaderCategories_button__Lv0HF')
    CATEGORIES_MENU_LIST = (By.CLASS_NAME, '.CategoriesMenu_list__KhAN+')
    CATEGORIES_FILTER_BUTTON = (By.CSS_SELECTOR, 'li.FilterButton_filter_button__o01GN')
    LAST_NEWS_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/news"]')
    TUTORIALS_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/tutorials"]')
    SELL_ON_ABRA_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/sell"]')
    CONTACT_SUPPORT_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/contact"]')
    FAQ_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/faq"]')
    LINK_CONTACT_SUPPORT_FROM_FAQ_PAGE = (By.CSS_SELECTOR, 'a.FAQ_link_text__jvPZN[href="/contact"]')
    ABOUT_US_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/about"]')
    LANGUAGE_AND_CURRENCY_MENU_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/header/div[2]/div[3]/div/div[1]/div')
    SHIPMENT_COUNTRY_MENU_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/header/div[2]/div[3]/div/div[2]/div/div')
