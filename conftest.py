import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")

    # Закрываем куки, если есть
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()=да все привыкли]"))
        )
        cookie_button.click()
    except:
        pass

    yield driver
    driver.quit()
