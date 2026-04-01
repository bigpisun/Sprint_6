from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    
    # Кнопки заказа
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    
    # FAQ
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__button']")
    
    @staticmethod
    def faq_answer(index):
        """Динамический локатор для ответа на вопрос FAQ по индексу"""
        return (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")

    # Кнопка согласия с куки
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
