from data_user import DataUser
from locators.base_page_locators import BasePageLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    def click_to_link_forgot_password(self):
        self.wait_visibility_element(BasePageLocators.TITLE_LOGIN)
        self.click_to_element(PasswordRecoveryPageLocators.FORGOT_PASSWORD_LINK)

    def get_text_title_reset_password_page(self):
        password_recovery_title = self.get_text(PasswordRecoveryPageLocators.RESET_PASSWORD_TITLE)
        return password_recovery_title

    def send_email_in_input(self):
        self.send_data(BasePageLocators.EMAIL_INPUT, DataUser.LOGIN_USER)

    def click_to_button_reset_password(self):
        self.click_to_element(PasswordRecoveryPageLocators.RESET_PASSWORD_BUTTON)

    def get_current_url_page_of_reset_password(self):
        self.wait_visibility_element(PasswordRecoveryPageLocators.SAVE_DATA_BUTTON)
        current_url = self.get_current_url()
        return current_url

    def wait_title_of_reset_password_page(self):
        self.wait_visibility_element(PasswordRecoveryPageLocators.RESET_PASSWORD_TITLE)

    def click_to_icon_show_password(self):
        self.click_to_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    def get_attribute_by_active_class_of_input(self):
        active_class_input = self.get_attribute_by_class(PasswordRecoveryPageLocators.INPUT_NEW_PASSWORD)
        return active_class_input
