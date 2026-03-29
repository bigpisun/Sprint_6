from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderPage(BasePage):
    # Локаторы — первого шага
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы — второго шага
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Сообщение об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
    
    def fill_first_form(self, data):
        """Заполнение первой формы заказа"""
        self.send_keys(self.NAME_FIELD, data['name'])
        self.send_keys(self.SURNAME_FIELD, data['surname'])
        self.send_keys(self.ADDRESS_FIELD, data['address'])
        
        # Выбор станции метро
        self.click_element(self.METRO_FIELD)
        metro_locator = (By.XPATH, f"//div[text()='{data['metro']}']")
        self.click_element(metro_locator)
        
        self.send_keys(self.PHONE_FIELD, data['phone'])
        self.click_element(self.NEXT_BUTTON)
    
    def fill_second_form(self, data):
        """Заполнение второй формы заказа"""
        # Дата
        self.send_keys(self.DATE_FIELD, data['date'])
        self.driver.find_element(*self.DATE_FIELD).click()
        
        # Срок аренды
        self.click_element(self.RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[text()='{data['rental_period']}']")
        self.click_element(period_locator)
        
        # Цвет
        if data['color'] == 'чёрный жемчуг':
            self.click_element(self.COLOR_BLACK)
        elif data['color'] == 'серая безысходность':
            self.click_element(self.COLOR_GREY)
        
        # Комментарий
        self.send_keys(self.COMMENT_FIELD, data['comment'])
        self.click_element(self.ORDER_BUTTON)
    
    def confirm_order(self):
        """Подтверждение заказа"""
        self.click_element(self.CONFIRM_BUTTON)
    
    def is_order_successful(self):
        """Проверка успешного оформления заказа"""
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).is_displayed()