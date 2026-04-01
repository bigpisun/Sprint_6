from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы заказа"""
    
    # Первая форма
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая форма
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.XPATH, "//label[text()='чёрный жемчуг']")
    COLOR_GREY = (By.XPATH, "//label[text()='серая безысходность']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
    
    @staticmethod
    def metro_option(metro_name):
        """Динамический локатор для выбора станции метро"""
        return (By.XPATH, f"//div[contains(@class, 'Order_SelectOption') and text()='{metro_name}']")
    
    @staticmethod
    def rental_period_option(period):
        """Динамический локатор для выбора срока аренды"""
        return (By.XPATH, f"//div[text()='{period}']")
