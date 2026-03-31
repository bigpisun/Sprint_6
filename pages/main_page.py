from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__button']")

    def get_faq_answer(self, index):
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")
        return self.get_text(answer_locator)

    def click_faq_question(self, index):
        questions = self.wait.until(EC.presence_of_all_elements_located(self.FAQ_QUESTIONS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", questions[index])
        self.driver.execute_script("arguments[0].click();", questions[index])

    def click_order_top_button(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    def click_order_bottom_button(self):
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        element = self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO))
        element.click()
        self.wait.until(lambda d: len(d.window_handles) > 1)