from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    def select_metro(self, metro_name):
        """Выбор станции метро"""
        metro_input = self.wait.until(EC.element_to_be_clickable(self.locators.METRO_FIELD))
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro_name)
        metro_input.send_keys(Keys.DOWN)
        metro_input.send_keys(Keys.ENTER)

    def select_rental_period(self, period):
        """Выбор срока аренды"""
        self.js_click(self.locators.RENTAL_PERIOD)
        period_option = self.locators.rental_period_option(period)
        self.js_click(period_option)

    def select_color(self, color):
        """Выбор цвета самоката"""
        if color == 'чёрный жемчуг':
            self.click_element(self.locators.COLOR_BLACK)
        else:
            self.click_element(self.locators.COLOR_GREY)

    def fill_first_form(self, data):
        """Заполнение первой формы заказа"""
        self.send_keys(self.locators.NAME_FIELD, data['name'])
        self.send_keys(self.locators.SURNAME_FIELD, data['surname'])
        self.send_keys(self.locators.ADDRESS_FIELD, data['address'])
        self.select_metro(data['metro'])
        self.send_keys(self.locators.PHONE_FIELD, data['phone'])
        self.click_element(self.locators.NEXT_BUTTON)

    def fill_second_form(self, data):
        """Заполнение второй формы заказа"""
        self.send_keys(self.locators.DATE_FIELD, data['date'])
        self.select_rental_period(data['rental_period'])
        self.select_color(data['color'])
        self.send_keys(self.locators.COMMENT_FIELD, data['comment'])
        self.click_element(self.locators.ORDER_BUTTON)
        self.click_element(self.locators.CONFIRM_BUTTON)

    def is_order_successful(self):
        """Проверка успешного оформления заказа"""
        return self.wait.until(EC.visibility_of_element_located(self.locators.SUCCESS_MESSAGE)).is_displayed()
