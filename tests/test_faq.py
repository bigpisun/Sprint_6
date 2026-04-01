import allure
import pytest
from data.test_data import TestData


@allure.feature('FAQ')
class TestFAQ:
    
    @allure.title('Проверка текста ответа на вопрос: {question_data[question]}')
    @pytest.mark.parametrize('question_data', TestData.FAQ_DATA)
    def test_faq_answers(self, main_page, question_data):
        index = TestData.FAQ_DATA.index(question_data)
        
        with allure.step(f'Клик на вопрос: {question_data["question"]}'):
            main_page.click_faq_question(index)
        
        with allure.step('Проверка текста ответа'):
            actual_answer = main_page.get_faq_answer(index)
            assert actual_answer == question_data['answer']
