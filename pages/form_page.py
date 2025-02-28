from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    # Получение имени
    def fill_name(self, name):
        name_input = self.driver.find_element(By.CSS_SELECTOR, "#name-input")
        name_input.send_keys(name)

    # Получение пароля
    def fill_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(password)

    # Выбор любимого напитка
    def select_favorite_drinks(self):
        milk_checkbox = self.driver.find_element(By.ID, "drink2")
        coffee_checkbox = self.driver.find_element(By.ID, "drink3")
        milk_checkbox.click()
        coffee_checkbox.click()

    # Выбор любимого цвета
    def select_favorite_color(self):
        try:
            yellow_radio = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "color3"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", yellow_radio)
            self.driver.execute_script("arguments[0].click();", yellow_radio)
        except Exception as e:
            print(f"Ошибка при выборе цвета: {e}")

    # Выбор случайного варианта
    def select_random_automation_option(self):
        select_element = Select(self.driver.find_element(By.ID, "automation"))
        options = select_element.options
        valid_options = [option for option in options if option.get_attribute('value') != 'default']
        if valid_options:
            random_option = random.choice(valid_options)
            select_element.select_by_visible_text(random_option.text)

    # Получение поля
    def fill_email(self, email):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)

    # Ввод сообщения
    def fill_message(self, tools):
        message_input = self.driver.find_element(By.ID, "message")
        message_text = f"{len(tools)} tools: {max(tools, key=len)}"
        message_input.send_keys(message_text)

    # Сабмит
    def submit_form(self):
        try:
            submit_button = self.driver.find_element(By.ID, "submit-btn")
            self.driver.execute_script("arguments[0].click();", submit_button)

            print("Форма успешно отправлена.")
        except Exception as e:
            print(f"Ошибка при отправке формы: {e}")

    def check_alert_message(self):
        try:
            alert_obj = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            msg = alert_obj.text
            print("Полученный алерт:",msg)
            assert msg == "Message received!", "Сообщение не совпадает с ожидаемым!"
            alert_obj.accept()
        except NoAlertPresentException:
            print("Алерт не присутствует.")
        except Exception as e:
            print(f"Ошибка при проверке текста алерта: {e}")

