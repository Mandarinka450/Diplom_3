import allure
from pages.main_page import MainPage
from urls import UrlsPage


class TestMainPage:
    @allure.title('Переход по клику на страницу «Конструктор»')
    @allure.description('Проверка, что при клике на ссылку открывается соответствующая страница')
    def test_click_to_section_constructor(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
        main_page.open_page()
        main_page.click_to_link_of_constructor_page()
        title_page = main_page.get_title_of_constructor_page()
        assert title_page == 'Соберите бургер'

    @allure.title('Переход по клику на страницу «Лента заказов»')
    @allure.description('Проверка, что при клике на ссылку открывается соответствующая страница')
    def test_click_to_section_ribbon_of_orders(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.click_to_link_of_ribbon_orders_page()
        title_page = main_page.get_title_of_ribbon_orders_page()
        assert title_page == 'Лента заказов'

    @allure.title('Открытие всплывающего окна при клике на ингредиент')
    @allure.description('Проверка, что при клике на ингредиент открывается всплывающее окно с информацией')
    def test_open_modal_window_details_of_ingredients(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.wait_title_of_page()
        main_page.click_to_card_of_ingredient()
        check_modal_window_is_opened = main_page.get_attribute_by_class_of_opened_modal_window()
        assert check_modal_window_is_opened is True

    @allure.title('Закрытие всплывающего окна при клике на соответствующую иконку')
    @allure.description('Проверка, что при клике на иконку крестика закрывается окно с информацией')
    def test_close_modal_window_details_of_ingredients_by_click_on_cross_button(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.wait_title_of_page()
        main_page.click_to_card_of_ingredient()
        main_page.close_modal_window_details_of_ingredients_by_click_to_cross_button()
        check_modal_window_is_closed = main_page.get_attribute_by_class_of_closed_modal_window()
        assert check_modal_window_is_closed is False

    @allure.title('Увеличение каунтера при добавлении ингредиента в заказ')
    @allure.description('Проверка, что если добавить ингредиент в заказ, то его каунтер увеличивается')
    def test_add_ingredient_in_order_and_increase_counter(self, driver):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.wait_title_of_page()
        main_page.move_ingredient_from_source_to_destination()
        counter = main_page.get_counter_of_added_ingredient()
        assert counter == '2'

    @allure.title('Оформление заказа')
    @allure.description('Проверка, что залогиненный пользователь может оформить заказ')
    def test_create_success_order(self, driver, login):
        main_page = MainPage(driver, UrlsPage.BASE_URL)
        main_page.open_page()
        main_page.move_ingredient_from_source_to_destination()
        main_page.click_to_create_order_button()
        main_page.wait_id_of_created_order()
        text_create_order = main_page.get_text_about_created_order()
        assert text_create_order == 'Ваш заказ начали готовить'
