from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'register form is not presented'

    def register_new_user(self, email='test@mail.ru', password='password'):
        email_btn = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        email_btn.send_keys(email)
        password_btn = self.browser.find_element(*LoginPageLocators.PASSWORD_REG)
        password_btn.send_keys(password)
        password_confirmation = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION)
        password_confirmation.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        reg_button.click()
