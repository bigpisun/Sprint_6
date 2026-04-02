from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    def click_order_top_button(self):
        """Клик по верхней кнопке заказа"""
        self.click_element(self.locators.ORDER_TOP_BUTTON)

    def click_order_bottom_button(self):
        """Клик по нижней кнопке заказа"""
        self.click_element(self.locators.ORDER_BOTTOM_BUTTON)

    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(self.locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.js_click(self.locators.YANDEX_LOGO)
        self.wait_for_new_window(2)

    def click_faq_question(self, index):
        """Клик по вопросу FAQ по индексу"""
        questions = self.wait_for_elements(self.locators.FAQ_QUESTIONS)
        self.js_scroll_and_click(questions[index])

    def get_faq_answer(self, index):
        """Получить текст ответа на вопрос по индексу"""
        return self.get_text(self.locators.faq_answer(index))
