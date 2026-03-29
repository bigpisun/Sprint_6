import allure
import pytest
from pages.main_page import MainPage
from helpers.data import TestData


@allure.feature("FAQ")
class TestFAQ:
    
    @allure.title("Проверка текста ответа на вопрос")
    @pytest.mark.parametrize("question_data", TestData.FAQ_DATA)
    def test_faq_answers(self, driver, question_data):
        main_page = MainPage(driver)
        index = TestData.FAQ_DATA.index(question_data)
        
        with allure.step(f"Клик на вопрос: {question_data["question"]}"):
            main_page.click_faq_question(index)
        
        with allure.step("Проверка текста ответа"):
            actual_answer = main_page.get_faq_answer(index)
            assert actual_answer == question_data["answer"]
