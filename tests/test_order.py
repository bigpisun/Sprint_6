import allure
import pytest
from data.test_data import TestData


@allure.feature('Заказ самоката')
class TestOrder:
    
    @allure.title('Заказ самоката с верхней кнопкой (набор данных 1)')
    def test_order_top_button_data_1(self, driver, main_page, order_page):
        data = TestData.ORDER_DATA[0]
        
        with allure.step('Нажатие на верхнюю кнопку заказа'):
            main_page.click_order_top_button()
        
        with allure.step('Заполнение первой формы'):
            order_page.fill_first_form(data)
        
        with allure.step('Заполнение второй формы'):
            order_page.fill_second_form(data)
        
        with allure.step('Проверка успешного оформления'):
            assert order_page.is_order_successful()
    
    @allure.title('Заказ самоката с верхней кнопкой (набор данных 2)')
    def test_order_top_button_data_2(self, driver, main_page, order_page):
        data = TestData.ORDER_DATA[1]
        
        with allure.step('Нажатие на верхнюю кнопку заказа'):
            main_page.click_order_top_button()
        
        with allure.step('Заполнение первой формы'):
            order_page.fill_first_form(data)
        
        with allure.step('Заполнение второй формы'):
            order_page.fill_second_form(data)
        
        with allure.step('Проверка успешного оформления'):
            assert order_page.is_order_successful()
    
    @allure.title('Заказ самоката с нижней кнопкой (набор данных 1)')
    def test_order_bottom_button_data_1(self, driver, main_page, order_page):
        data = TestData.ORDER_DATA[0]
        
        with allure.step('Нажатие на нижнюю кнопку заказа'):
            main_page.click_order_bottom_button()
        
        with allure.step('Заполнение первой формы'):
            order_page.fill_first_form(data)
        
        with allure.step('Заполнение второй формы'):
            order_page.fill_second_form(data)
        
        with allure.step('Проверка успешного оформления'):
            assert order_page.is_order_successful()
    
    @allure.title('Заказ самоката с нижней кнопкой (набор данных 2)')
    def test_order_bottom_button_data_2(self, driver, main_page, order_page):
        data = TestData.ORDER_DATA[1]
        
        with allure.step('Нажатие на нижнюю кнопку заказа'):
            main_page.click_order_bottom_button()
        
        with allure.step('Заполнение первой формы'):
            order_page.fill_first_form(data)
        
        with allure.step('Заполнение второй формы'):
            order_page.fill_second_form(data)
        
        with allure.step('Проверка успешного оформления'):
            assert order_page.is_order_successful()
    
    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, main_page):
        current_url = main_page.driver.current_url
        
        with allure.step('Клик на логотип Самоката'):
            main_page.click_scooter_logo()
        
        with allure.step('Проверка URL'):
            assert main_page.driver.current_url == current_url
    
    @allure.title('Проверка открытия Дзена по логотипу Яндекса')
    def test_yandex_logo_redirect(self, main_page):
        current_window = main_page.driver.current_window_handle
        
        with allure.step('Клик на логотип Яндекса'):
            main_page.click_yandex_logo()
        
        with allure.step('Переключение на новую вкладку'):
            main_page.switch_to_new_window(current_window)
        
        with allure.step('Проверка URL'):
            assert 'dzen.ru' in main_page.driver.current_url
