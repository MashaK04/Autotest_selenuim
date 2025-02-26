import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage


def test_form_submission():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://practice-automation.com/form-fields/")

        form_page = FormPage(driver)
        # Заполнение формы
        form_page.fill_name("Test User")
        form_page.fill_password("password123")
        form_page.select_favorite_drinks()
        form_page.select_favorite_color()
        form_page.select_random_automation_option()

        # Заполнение email
        form_page.fill_email("name@example.com")

        automation_tools_list = driver.find_element(By.XPATH,
                                                    "//label[text()='Automation tools']/following-sibling::ul")
        list_items = automation_tools_list.find_elements(By.TAG_NAME, "li")
        tools = [item.text for item in list_items]
        form_page.fill_message(tools)

        # Отправка формы
        time.sleep(10)
        form_page.submit_form()


    finally:
        time.sleep(2)
        driver.quit()