from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.ribbon_orders_page_locators import RibbonOrdersPageLocators
from pages.base_page import BasePage


class RibbonOrdersPage(BasePage):
    def wait_title_of_ribbon_orders_page(self):
        self.wait_visibility_element(MainPageLocators.TITLE_RIBBON_ORDERS)

    def click_to_link_personal_account(self):
        self.click_to_element(BasePageLocators.PERSONAL_ACCOUNT)

    def click_to_history_orders(self):
        self.click_to_element(BasePageLocators.LINK_HISTORY_ORDER)

    def get_expected_number_order_in_history(self):
        number = self.get_text(BasePageLocators.NUMBER_OF_ORDER)
        return number

    def get_all_number_of_orders(self):
        orders = []
        numbers = self.get_all_elements(RibbonOrdersPageLocators.NUMBERS_OF_ORDERS)
        for value in numbers:
            orders.append(value.text)
        return orders

    def check_number_of_order_on_ribbons_page(self, orders, number):
        for item in orders:
            if item == number:
                return True
            else:
                break

    def click_to_card_of_order(self):
        self.click_to_element(MainPageLocators.CARD_ORDER)

    def get_active_class_of_open_modal_window(self):
        class_open = self.get_attribute_by_class(MainPageLocators.SECTION_MODAL_WINDOW_ORDER)
        check = self.check_open('Modal_modal_opened__3ISw4', class_open)
        return check

    def get_expected_number_of_order(self):
        expected_number = self.get_text(MainPageLocators.NUMBER_ORDER)
        return expected_number

    def wait_until_locator_is_not_none(self):
        self.wait_until_locator_is_not(MainPageLocators.LI_NUMBER_ORDERS)

    def get_actual_number_of_order(self):
        actual_number = self.get_text(MainPageLocators.LI_NUMBER_ORDERS)
        return actual_number

    def click_to_link_ribbon_orders_page(self):
        self.click_to_element(MainPageLocators.LINK_RIBBON_ORDERS)

    def get_old_value_of_quantity_completed_orders_on_all_day(self):
        old = self.get_text(RibbonOrdersPageLocators.COMPLETE_DAY)
        int(old)
        return old

    def click_to_link_of_constructor_page(self):
        self.click_to_element(MainPageLocators.LINK_CONSTRUCTOR)

    def move_ingredient_from_source_to_destination(self):
        source1 = self.wait_to_clickable_element(MainPageLocators.CARD_ROLL)
        source2 = self.wait_to_clickable_element(MainPageLocators.DESTINATION)
        self.drag_and_drop_element(source1, source2)

    def click_to_create_order_button(self):
        self.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER)

    def wait_id_completed_order(self):
        self.wait_until_text_is_not(MainPageLocators.NUMBER_ORDER, '9999')

    def click_to_close_opened_window_of_completed_order(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_WINDOW)

    def get_new_value_of_quantity_completed_orders_on_all_day(self):
        new = self.get_text(RibbonOrdersPageLocators.COMPLETE_DAY)
        int(new)
        return new

    def get_old_value_of_quantity_completed_orders_on_all_time(self):
        old = self.get_text(RibbonOrdersPageLocators.COMPLETE_ALL_TIME)
        return old

    def get_new_value_of_quantity_completed_orders_on_all_time(self):
        new = self.get_text(RibbonOrdersPageLocators.COMPLETE_ALL_TIME)
        return new
