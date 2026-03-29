import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers.data import TestData


@allure.feature('Заказ самоката')
class TestOrder:
    
    @allure.title('Позитивный сценарий заказа самоката')
    @pytest.mark.parametrize('order_data', TestData.ORDER_DATA)
    @pytest.mark.parametrize('button_type', ['top', 'bottom'])
    def test_successful_order(self, driver, order_data, button_type):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step(f'Нажатие на кнопку заказа ({button_type})'):
            if button_type == 'top':
                main_page.click_order_top_button()
            else:
                main_page.click_order_bottom_button()
        
        with allure.step('Заполнение первой формы'):
            order_page.fill_first_form(order_data)
        
        with allure.step('Заполнение второй формы'):
            order_page.fill_second_form(order_data)
        
        with allure.step('Подтверждение заказа'):
            order_page.confirm_order()
        
        with allure.step('Проверка успешного оформления'):
            assert order_page.is_order_successful(), 'Заказ не был оформлен'
    
    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Клик на логотип Самоката'):
            main_page.click_scooter_logo()
        
        with allure.step('Проверка URL'):
            assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
    
    @allure.title('Проверка открытия Дзена по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        
        with allure.step('Клик на логотип Яндекса'):
            main_page.click_yandex_logo()
        
        with allure.step('Переключение на новую вкладку'):
            driver.switch_to.window(driver.window_handles[1])
        
        with allure.step('Проверка URL'):
            assert 'dzen.ru' in driver.current_url