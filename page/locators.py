from selenium.webdriver.common.by import By

class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, "a[href='/ru/basket/']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Ваша корзина пуста')]")

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

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

