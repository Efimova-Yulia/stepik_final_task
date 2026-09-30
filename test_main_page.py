from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.locators import LoginPageLocators, MainPageLocators
from page.login_page import LoginPage
from page.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    browser.find_element(*MainPageLocators.LOGIN_LINK).click()


    login_page = LoginPage(browser,browser.current_url)
    wait=WebDriverWait(browser,10)

    wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM))
    login_page.should_be_login_form()
    login_page.should_be_login_url()
    login_page.should_be_register_form()
