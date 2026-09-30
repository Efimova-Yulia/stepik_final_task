from selenium.webdriver.common.by import By

class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")

class RegisterPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")
