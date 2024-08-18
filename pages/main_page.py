from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_link_of_constructor_page(self):
        self.click_to_element(MainPageLocators.LINK_CONSTRUCTOR)

    def get_title_of_constructor_page(self):
        title_constructor = self.get_text(BasePageLocators.TITLE_CONSTRUCTOR)
        return title_constructor

    def click_to_link_of_ribbon_orders_page(self):
        self.click_to_element(MainPageLocators.LINK_RIBBON_ORDERS)

    def get_title_of_ribbon_orders_page(self):
        title_ribbon_of_orders = self.get_text(MainPageLocators.TITLE_RIBBON_ORDERS)
        return title_ribbon_of_orders

    def wait_title_of_page(self):
        self.wait_visibility_element(BasePageLocators.TITLE_CONSTRUCTOR)

    def click_to_card_of_ingredient(self):
        self.click_to_element(MainPageLocators.CARD_ROLL)

    def get_attribute_by_class_of_opened_modal_window(self):
        class_open = self.get_attribute_by_class(MainPageLocators.SECTION_MODAL_WINDOW)
        check = self.check_open('Modal_modal_opened__3ISw4', class_open)
        return check

    def close_modal_window_details_of_ingredients_by_click_to_cross_button(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_WINDOW)

    def get_attribute_by_class_of_closed_modal_window(self):
        class_close = self.get_attribute_by_class(MainPageLocators.SECTION_MODAL_WINDOW)
        check = self.check_open('Modal_modal_opened__3ISw4', class_close)
        return check

    def move_ingredient_from_source_to_destination(self):
        source1 = self.wait_to_clickable_element(MainPageLocators.CARD_ROLL)
        source2 = self.wait_to_clickable_element(MainPageLocators.DESTINATION)
        self.drag_and_drop_element(source1, source2)

    def get_counter_of_added_ingredient(self):
        counter = self.get_text(MainPageLocators.COUNTER)
        return counter

    def click_to_create_order_button(self):
        self.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER)

    def wait_id_of_created_order(self):
        self.wait_visibility_element(MainPageLocators.ID_ORDER)

    def get_text_about_created_order(self):
        text_create_order = self.get_text(MainPageLocators.TEXT_CREATE_ORDER)
        return text_create_order

