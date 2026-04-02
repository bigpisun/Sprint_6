from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        """Клик по элементу с прокруткой"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        """Ввод текста с очисткой поля"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def js_click(self, locator):
        """Клик через JavaScript (обходит перекрытия)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def js_scroll_and_click(self, element):
        """Скролл к элементу и клик через JavaScript"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_elements(self, locator):
        """Получить все элементы по локатору"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_new_window(self, expected_windows=2):
        """Ожидание открытия новой вкладки"""
        self.wait.until(lambda d: len(d.window_handles) == expected_windows)

    def switch_to_new_window(self, current_window):
        """Переключение на новую вкладку"""
        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def get_current_window_handle(self):
        """Получить текущий handle окна"""
        return self.driver.current_window_handle

    def accept_cookies(self, cookie_button_locator):
        """Закрыть куки, если есть"""
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(cookie_button_locator))
            cookie_button.click()
        except:
            pass
