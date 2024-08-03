from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_login_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    assert browser.current_url == 'https://dev.abra-market.com/login'


def test_go_to_registration_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_registration_page()
    assert browser.current_url == 'https://dev.abra-market.com/register'


def test_show_categories_menu_list(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.show_categories_menu_list()
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located(MainPageLocators.CATEGORIES_FILTER_BUTTON))


def test_go_to_news_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_news_page()
    assert browser.current_url == 'https://dev.abra-market.com/news'


def test_go_to_tutorials_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_tutorials_page()
    assert browser.current_url == 'https://dev.abra-market.com/tutorials'


def test_go_to_sell_on_abra_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_sell_on_abra_page()
    assert browser.current_url == 'https://dev.abra-market.com/sell'
    assert browser.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/h2')


def test_go_to_contact_support_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_contact_support_page()
    assert browser.current_url == 'https://dev.abra-market.com/contact'
    assert browser.find_element(By.CLASS_NAME, 'WhatsappPhoneNumber_phone_number__9IzKq')
    assert browser.find_elements(By.CLASS_NAME, 'SocialNetworks_network__d03A9')


def test_go_to_faq_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_faq_page()
    assert browser.current_url == 'https://dev.abra-market.com/faq'
    assert browser.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/h2')


def test_go_to_contact_support_from_faq_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_faq_page()
    page.go_to_contact_support_from_faq_page()
    assert browser.current_url == 'https://dev.abra-market.com/contact'


def test_go_to_about_us_page(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_about_us_page()
    assert browser.current_url == 'https://dev.abra-market.com/about'
    assert browser.find_element(By.XPATH, "//h2[text()=\"About Us\"]")


def test_language_and_currency_dropdown(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.language_and_currency_dropdown()
    dropdown_elements = browser.find_elements(By.CSS_SELECTOR, 'li.SelectItem_item__kFdkV[role="option"]')
    assert dropdown_elements
    assert len(dropdown_elements) == 2


def test_shipment_country_dropdown(browser):
    link = 'https://dev.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.shipment_country_dropdown()
    assert browser.find_elements(By.CSS_SELECTOR, 'li.SelectItem_item__kFdkV[role="option"]')
