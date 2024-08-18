import allure
from pages.personal_account_page import PersonalAccountPage
from urls import UrlsPage


class TestPersonalAccountPage:
    @allure.title('Выход из аккаунта')
    @allure.description('Проверка, что при выходе из аккаунта идет редирект на страницу входа')
    def test_logout_user(self, driver, login):
        personal_account_page = PersonalAccountPage(driver, UrlsPage.BASE_URL)
        personal_account_page.open_page()
        personal_account_page.click_to_link_of_personal_account()
        personal_account_page.click_to_logout_button()
        title_login = personal_account_page.get_title_of_login_page()
        assert title_login == 'Вход'

    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверка, что при клике на ссылку открывается соответствующая страница')
    def test_switch_to_personal_account(self, driver, login):
        personal_account_page = PersonalAccountPage(driver, UrlsPage.BASE_URL)
        personal_account_page.open_page()
        personal_account_page.click_to_link_of_personal_account()
        current_url = personal_account_page.get_current_url_of_page()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.PROFILE_PAGE

    @allure.title('Переход по клику на «История заказов»')
    @allure.description('Проверка, что при клике на ссылку открывается соответствующий раздел в личном кабинете')
    def test_switch_to_section_of_history_orders_in_personal_account(self, driver, login):
        personal_account_page = PersonalAccountPage(driver, UrlsPage.BASE_URL)
        personal_account_page.open_page()
        personal_account_page.click_to_link_of_personal_account()
        personal_account_page.click_to_link_history_of_orders()
        current_url = personal_account_page.get_current_url_of_page()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.HISTORY_OF_ORDERS_PAGE
