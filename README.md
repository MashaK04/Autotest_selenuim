Практикум SDET: тестовое задание
Выполнила: Каширина Мария

В рамках проекта реализовано два класса для автотеста с использованием паттерна проектирования Page Object Model

1. В файле form_page.py реализован основной класс FormPage предназначен для автоматизации заполнения веб-формы с использованием библиотеки Selenium. Он включает методы для ввода имени, пароля и электронной почты, выбора любимых напитков и цвета, а также отправки формы и проверки сообщений алерта. 
2. В файле test_form.py находится функция test_form_submission. Функция test_form_submission() предназначена для автоматического тестирования отправки формы на веб-сайте practice-automation.com. Она использует библиотеку Selenium для взаимодействия с веб-страницей и библиотеку Allure для документирования шагов теста.

Результаты теста автоматически в директорию allure-result в виде json файлов, для большей читабельности можно воспользоваться файлов read_result.py. В этом файле реализован код для преобзования последнего полученного (в случае если тестов было несколько) в текстовый файл 

Для запуска автотеста необходимо: 
1. В терминале выполнить следующую команду **pytest --alluredir=allure-results**
2. Также необходимо установить бибилотеку   **pip3 install pendulum**  
3. Для преобзования отчета в текстовый форма после заверщения теста необходимо выполнить следующую команду: **python3 read_result.py**   

 
