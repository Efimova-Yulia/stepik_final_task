import math

from selenium.common import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser
from page.locators import MainPageLocators, ProductPageLocators


class BasePage():
    def __init__(self,browser,url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK,error_message= "Ссылка для входа отсутствует")

    def get_element(self, how, what):
        return self.browser.find_element(by=how,value=what)


    def is_element_present(self, how, what,error_message, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            raise AssertionError(error_message)


    def is_element_not_present(self, how, what, error_message, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            raise AssertionError(error_message)


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def go_to_basket_page(self):
        link = self.browser.find_element(*MainPageLocators.BUTTON_BASKET)
        link.click()






