from selenium.webdriver.common.by import By


class RibbonOrdersPageLocators:
    COMPLETE_DAY = (By.XPATH, './/p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')
    COMPLETE_ALL_TIME = (By.XPATH, './/p[contains(text(), "Выполнено за все время")]/following-sibling::p')
    NUMBERS_OF_ORDERS = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]//p[@class="text text_type_digits-default"]')