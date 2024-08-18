from selenium.webdriver.common.by import By


class BasePageLocators:
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/following-sibling::input')  # инпут для ввода почты
    PASSWORD_INPUT = (By.XPATH, './/*[text()="Пароль"]/following-sibling::input')  # инпут для ввода пароля
    LOGIN_BUTTON = (By.XPATH, './/button[contains(text(), "Войти")]')  # кнопка "Войти"
    PERSONAL_ACCOUNT = (By.XPATH, './/p[contains(text(), "Личный Кабинет")]/parent::a')  # ссылка "Личный кабинет"
    TITLE_CONSTRUCTOR = (By.XPATH, './/h1[contains(text(), "Соберите бургер")]')  # заголовок конструктора
    TITLE_LOGIN = (By.XPATH, './/div[@class="Auth_login__3hAey"]/h2[contains(text(), "Вход")]')  # заголовок "Вход"
    LINK_HISTORY_ORDER = (By.XPATH, './/a[contains(text(), "История заказов")]')  # ссылка на историю заказов в личном кабинете
    NUMBER_OF_ORDER = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][last()]//p[@class="text text_type_digits-default"]')  # номер заказа