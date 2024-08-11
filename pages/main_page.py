import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators, FaqPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_registration_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTRATION_LINK)
        register_link.click()

    def show_categories_menu_list(self):
        all_categories_link = self.browser.find_element(*MainPageLocators.All_CATEGORIES_MENU_ITEM)
        all_categories_link.click()

    def display_clothes_category_items(self):
        self.show_categories_menu_list()
        categories_menu_option = self.browser.find_element(*MainPageLocators.CLOTHES_CATEGORY_MENU_OPTION)
        ActionChains(self.browser).move_to_element(categories_menu_option).perform()

    def go_to_product_category_page(self):
        self.display_clothes_category_items()
        subcategory_items = self.browser.find_elements(*MainPageLocators.SUBCATEGORY_ITEMS)
        subcategory_items[0].click()

    def go_to_news_page(self):
        self.browser.find_element(*MainPageLocators.LAST_NEWS_MENU_ITEM).click()

    def go_to_tutorials_page(self):
        self.browser.find_element(*MainPageLocators.TUTORIALS_MENU_ITEM).click()

    def go_to_sell_on_abra_page(self):
        self.browser.find_element(*MainPageLocators.SELL_ON_ABRA_MENU_ITEM).click()

    def go_to_contact_support_page(self):
        self.browser.find_element(*MainPageLocators.CONTACT_SUPPORT_MENU_ITEM).click()

    def go_to_faq_page(self):
        self.browser.find_element(*MainPageLocators.FAQ_MENU_ITEM).click()

    def go_to_contact_support_from_faq_page(self):
        self.browser.find_element(*FaqPageLocators.LINK_CONTACT_SUPPORT_FROM_FAQ_PAGE).click()

    def go_to_about_us_page(self):
        self.browser.find_element(*MainPageLocators.ABOUT_US_MENU_ITEM).click()

    def language_and_currency_dropdown(self):
        self.browser.find_element(*MainPageLocators.LANGUAGE_AND_CURRENCY_MENU_DROPDOWN).click()

    def shipment_country_dropdown(self):
        self.browser.find_element(*MainPageLocators.SHIPMENT_COUNTRY_MENU_DROPDOWN).click()
