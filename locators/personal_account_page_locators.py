from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    LOGOUT_BUTTON = (By.XPATH, './/button[contains(text(), "Выход")]')  # кнопка "Выход"
    HISTORY_ORDER_TITLE = (By.XPATH, './/a[contains(text(), "История заказов")]')  # ссылка на профиль
