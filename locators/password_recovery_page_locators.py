from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, './/a[contains(text(), "Восстановить пароль")]')  # ссылка на восстановление пароля
    RESET_PASSWORD_TITLE = (By.XPATH, './/h2[contains(text(), "Восстановление пароля")]')  # заголовок страницы восстановления пароля
    RESET_PASSWORD_BUTTON = (By.XPATH, './/button[contains(text(), "Восстановить")]') # кнопка, которая переходит на страницу создания пароля
    SAVE_DATA_BUTTON = (By.XPATH, './/button[contains(text(), "Сохранить")]') # кнопка сохранения пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, './/div[@class="input__icon input__icon-action"]/*') # кнопка скрывает/показывает пароль
    INPUT_NEW_PASSWORD = (By.XPATH, './/label[contains(text(), "Пароль")]/parent::div') # инпут для ввода почты