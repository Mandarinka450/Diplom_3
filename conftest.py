from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data_user import DataUser
from locators.base_page_locators import BasePageLocators
from urls import UrlsPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(UrlsPage.BASE_URL + UrlsPage.LOGIN_PAGE)
    driver.find_element(*BasePageLocators.EMAIL_INPUT).send_keys(DataUser.LOGIN_USER)
    driver.find_element(*BasePageLocators.PASSWORD_INPUT).send_keys(DataUser.PASSWORD_USER)
    driver.find_element(*BasePageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(BasePageLocators.TITLE_CONSTRUCTOR))
