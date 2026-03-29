from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__item')]//div[contains(@class, 'accordion__button')]")
    
    def click_order_top_button(self):
        self.click_element(self.ORDER_TOP_BUTTON)
    
    def click_order_bottom_button(self):
        self.click_element(self.ORDER_BOTTOM_BUTTON)
    
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
    
    def click_faq_question(self, index):
        questions = self.driver.find_elements(*self.FAQ_QUESTIONS)
        questions[index].click()
    
    def get_faq_answer_text(self, index):
        answer_locator = (By.XPATH, f"//div[contains(@class, 'accordion__item')][{index+1}]//div[contains(@class, 'accordion__panel')]/p")
        return self.get_text(answer_locator)
