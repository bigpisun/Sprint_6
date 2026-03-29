import allure
import pytest
from pages.main_page import MainPage
from helpers.data import TestData


@allure.feature('FAQ')
class TestFAQ:
    
    @allure.title('Проверка текста ответа на вопрос "{question}"')
    @pytest.mark.parametrize('index, question, expected_answer', 
                             [(i, q['question'], q['answer']) for i, q in enumerate(TestData.FAQ_DATA)])
    def test_faq_answers(self, driver, index, question, expected_answer):
        main_page = MainPage(driver)
        
        with allure.step(f'Клик на вопрос: {question}'):
            main_page.click_faq_question(index)
        
        with allure.step('Проверка текста ответа'):
            actual_answer = main_page.get_faq_answer_text(index)
            assert actual_answer == expected_answer
