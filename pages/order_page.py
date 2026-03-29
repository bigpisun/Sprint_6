from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_FIELD = (By.XPATH, "//input[@placeholder="\"* Имя\""]")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder="\"* Фамилия\""]")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder="\"* Адрес: куда привезти заказ\""]")
    METRO_FIELD = (By.XPATH, "//input[@placeholder="\"* Станция метро\""]")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder="\"* Телефон: на него позвонит курьер\""]")
    NEXT_BUTTON = (By.XPATH, "//button[text()="\"Далее\""]")
    DATE_FIELD = (By.XPATH, "//input[@placeholder="\"* Когда привезти самокат\""]")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, "\"Dropdown-control\"")]")
    COLOR_BLACK = (By.XPATH, "//label[text()="\"чёрный жемчуг\""]")
    COLOR_GREY = (By.XPATH, "//label[text()="\"серая безысходность\""]")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder="\"Комментарий для курьера\""]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, "\"Button_Button__ra12g\"") and text()="\"Заказать\""]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()="\"Да\""]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, "\"Order_ModalHeader__3FDaJ\"") and text()="\"Заказ оформлен\""]")

    def select_metro(self, metro_name):
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_FIELD))
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro_name)
        metro_input.send_keys(Keys.DOWN)
        metro_input.send_keys(Keys.ENTER)

    def select_rental_period(self, period):
        dropdown = self.wait.until(EC.presence_of_element_located(self.RENTAL_PERIOD))
        self.driver.execute_script("arguments[0].click();", dropdown)
        period_option = (By.XPATH, f"//div[contains(@class, "\"Dropdown-option\"") and text()="\"{period}\""]")
        option = self.wait.until(EC.element_to_be_clickable(period_option))
        self.driver.execute_script("arguments[0].click();", option)

    def fill_first_form(self, data):
        self.send_keys(self.NAME_FIELD, data["name"])
        self.send_keys(self.SURNAME_FIELD, data["surname"])
        self.send_keys(self.ADDRESS_FIELD, data["address"])
        self.select_metro(data["metro"])
        self.send_keys(self.PHONE_FIELD, data["phone"])
        self.click_element(self.NEXT_BUTTON)

    def fill_second_form(self, data):
        self.send_keys(self.DATE_FIELD, data["date"])
        self.driver.find_element(*self.DATE_FIELD).click()
        self.select_rental_period(data["rental_period"])
        if data["color"] == "чёрный жемчуг":
            self.click_element(self.COLOR_BLACK)
        else:
            self.click_element(self.COLOR_GREY)
        self.send_keys(self.COMMENT_FIELD, data["comment"])
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)

    def is_order_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).is_displayed()
