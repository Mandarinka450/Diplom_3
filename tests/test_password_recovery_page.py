import allure
from pages.password_recovery_page import PasswordRecoveryPage
from urls import UrlsPage


class TestPasswordRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверка, что при клике на ссылку открывается соответствующая страница')
    def test_click_to_password_recovery_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver, UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
        password_recovery_page.open_page()
        password_recovery_page.click_to_link_forgot_password()
        password_recovery_title = password_recovery_page.get_text_title_reset_password_page()
        assert password_recovery_title == 'Восстановление пароля'

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Проверка, что осуществляется переход на соответствующую страницу по кнопке "Восстановить пароль"')
    def test_send_email_and_click_to_reset_password_button(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver, UrlsPage.BASE_URL + UrlsPage.FORGOT_PASSWORD_PAGE)
        password_recovery_page.open_page()
        password_recovery_page.send_email_in_input()
        password_recovery_page.click_to_button_reset_password()
        current_url = password_recovery_page.get_current_url_page_of_reset_password()
        assert current_url == UrlsPage.BASE_URL + UrlsPage.RESET_PASSWORD_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Проверка, что при клике на иконку показать/скрыть пароль появляется необходимый класс, который должен подсвечивать поле')
    def test_click_to_active_input_email(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver, UrlsPage.BASE_URL + UrlsPage.FORGOT_PASSWORD_PAGE)
        password_recovery_page.open_page()
        password_recovery_page.send_email_in_input()
        password_recovery_page.click_to_button_reset_password()
        password_recovery_page.wait_title_of_reset_password_page()
        password_recovery_page.click_to_icon_show_password()
        active_class = password_recovery_page.get_attribute_by_active_class_of_input()
        assert 'input_status_active' in active_class
