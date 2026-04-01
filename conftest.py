import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from data.urls import Urls


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия браузера"""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Firefox(options=options)
    driver.get(Urls.BASE_URL)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    """Фикстура для страницы заказа"""
    from pages.order_page import OrderPage
    return OrderPage(driver)


@pytest.fixture
def close_cookies(driver, main_page):
    """Фикстура для закрытия куки"""
    from locators.main_page_locators import MainPageLocators
    main_page.accept_cookies(MainPageLocators.COOKIE_BUTTON)
