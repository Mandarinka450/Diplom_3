from locators.base_page_locators import BasePageLocators
from locators.personal_account_page_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def click_to_link_of_personal_account(self):
        self.click_to_element(BasePageLocators.PERSONAL_ACCOUNT)

    def click_to_logout_button(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)

    def get_title_of_login_page(self):
        title_login = self.get_text(BasePageLocators.TITLE_LOGIN)
        return title_login

    def get_current_url_of_page(self):
        current_url = self.get_current_url()
        return current_url

    def click_to_link_history_of_orders(self):
        self.click_to_element(PersonalAccountLocators.HISTORY_ORDER_TITLE)