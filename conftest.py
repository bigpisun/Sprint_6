import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    """Фикстура для инициализации драйвера Firefox"""
    options = Options()
    options.add_argument('--window-size=1920,1080')
    # Раскомментируй для headless-режима:
    # options.add_argument('--headless')
    
    driver = webdriver.Firefox(options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()