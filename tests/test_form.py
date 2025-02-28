import time
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage
import os
import shutil

@allure.title("Тестирование отправки формы для практикума")
@allure.description("Тест проверяет функциональность отправки формы на сайте practice-automation.com")
def test_form_submission():

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    with allure.step("Открытие веб-страницы"):
        driver.get("https://practice-automation.com/form-fields/")

    form_page = FormPage(driver)

    #Заполнение формы
    with allure.step("Заполнение формы"):
        form_page.fill_name("Каширина Мария")
        form_page.fill_password("password123")
        form_page.select_favorite_drinks()
        form_page.select_favorite_color()
        form_page.select_random_automation_option()
        form_page.fill_email("MashaTest@test.ru")

        # Заполнение сообщения c получением списка
        automation_tools_list = driver.find_element(By.XPATH,
                                                    "//label[text()='Automation tools']/following-sibling::ul")
        list_items = automation_tools_list.find_elements(By.TAG_NAME, "li")
        tools = [item.text for item in list_items]
        form_page.fill_message(tools)

    with allure.step("Отправка формы"):
        time.sleep(5)
        form_page.submit_form()

    with allure.step("Проверка сообщения алерта"):
        form_page.check_alert_message()

    driver.quit()


if __name__ == "__main__":
    test_form_submission()
