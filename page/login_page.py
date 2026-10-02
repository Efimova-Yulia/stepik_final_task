from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес - подстрока "login" присутствует в текущем url
        assert 'login' in self.browser.current_url, "Login link is not presented in current url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.get_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.get_element(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True