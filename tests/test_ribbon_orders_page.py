import allure
from pages.ribbon_orders_page import RibbonOrdersPage
from urls import UrlsPage


class TestRibbonOrdersPage:
    @allure.title('Открытие всплывающего окна с информацией по заказу')
    @allure.description('Проверка, что при клике на карточку заказа открывается всплывающее окно с информацией')
    def test_open_modal_window_details_of_order(self, driver):
        ribbon_orders_page = RibbonOrdersPage(driver, UrlsPage.BASE_URL + UrlsPage.FEED_PAGE)
        ribbon_orders_page.open_page()
        ribbon_orders_page.wait_title_of_ribbon_orders_page()
        ribbon_orders_page.click_to_card_of_order()
        check_modal_window_is_open = ribbon_orders_page.get_active_class_of_open_modal_window()
        assert check_modal_window_is_open is True

    @allure.title('Заказы пользователя отображаются на странице "Лента заказов"')
    @allure.description('Проверка, что заказы пользователя из раздела "История заказов" в личном кабинете отображаются на странице "Лента заказов"')
    def test_ribbon_of_orders_page_has_order_user(self, driver, login):
        ribbon_orders_page = RibbonOrdersPage(driver, UrlsPage.BASE_URL)
        ribbon_orders_page.open_page()
        ribbon_orders_page.move_ingredient_from_source_to_destination()
        ribbon_orders_page.click_to_create_order_button()
        ribbon_orders_page.wait_id_completed_order()
        ribbon_orders_page.click_to_close_opened_window_of_completed_order()
        ribbon_orders_page.click_to_link_personal_account()
        ribbon_orders_page.click_to_history_orders()
        number_of_order = ribbon_orders_page.get_expected_number_order_in_history()
        ribbon_orders_page.click_to_link_ribbon_orders_page()
        ribbon_orders_page.wait_title_of_ribbon_orders_page()
        number_of_orders = ribbon_orders_page.get_all_number_of_orders()
        result = ribbon_orders_page.check_number_of_order_on_ribbons_page(number_of_orders, number_of_order)
        assert result is True

    @allure.title('Номер оформленного заказа появляется в разделе "В работе"')
    @allure.description('Проверка, что номер только что оформленного заказа отображается в разделе "В работе" на странице "Лента заказов"')
    def test_check_number_of_order_in_work_section(self, driver, login):
        main_page = RibbonOrdersPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.move_ingredient_from_source_to_destination()
        main_page.click_to_create_order_button()
        main_page.wait_id_completed_order()
        expected_number = main_page.get_expected_number_of_order()
        main_page.click_to_close_opened_window_of_completed_order()
        main_page.click_to_link_ribbon_orders_page()
        main_page.wait_until_locator_is_not_none()
        actual_number = main_page.get_actual_number_of_order()
        assert f'0{expected_number}' == actual_number

    @allure.title('При оформлении заказа счетчик "Выполнено за сегодня" увеличивается')
    @allure.description('Проверка, что если оформить заказ, то счетчик на странице "Лента заказов" увеличивается')
    def test_check_number_of_completed_orders_of_all_day(self, driver, login):
        ribbon_orders_page = RibbonOrdersPage(driver, UrlsPage.BASE_URL)
        ribbon_orders_page.open_page()
        ribbon_orders_page.click_to_link_ribbon_orders_page()
        ribbon_orders_page.wait_title_of_ribbon_orders_page()
        old = ribbon_orders_page.get_old_value_of_quantity_completed_orders_on_all_day()
        ribbon_orders_page.click_to_link_of_constructor_page()
        ribbon_orders_page.move_ingredient_from_source_to_destination()
        ribbon_orders_page.click_to_create_order_button()
        ribbon_orders_page.wait_id_completed_order()
        ribbon_orders_page.click_to_close_opened_window_of_completed_order()
        ribbon_orders_page.click_to_link_ribbon_orders_page()
        new = ribbon_orders_page.get_new_value_of_quantity_completed_orders_on_all_day()
        assert old < new

    @allure.title('При оформлении заказа счетчик "Выполнено за все время" увеличивается')
    @allure.description('Проверка, что если оформить заказ, то счетчик на странице "Лента заказов" увеличивается')
    def test_check_number_of_completed_orders_of_all_time(self, driver, login):
        ribbon_orders_page = RibbonOrdersPage(driver, UrlsPage.BASE_URL)
        ribbon_orders_page.open_page()
        ribbon_orders_page.click_to_link_ribbon_orders_page()
        ribbon_orders_page.wait_title_of_ribbon_orders_page()
        old = ribbon_orders_page.get_old_value_of_quantity_completed_orders_on_all_time()
        ribbon_orders_page.click_to_link_of_constructor_page()
        ribbon_orders_page.move_ingredient_from_source_to_destination()
        ribbon_orders_page.click_to_create_order_button()
        ribbon_orders_page.wait_id_completed_order()
        ribbon_orders_page.click_to_close_opened_window_of_completed_order()
        ribbon_orders_page.click_to_link_ribbon_orders_page()
        new = ribbon_orders_page.get_new_value_of_quantity_completed_orders_on_all_time()
        assert old < new
