import pendulum
import glob
import json
import os

# Поиск нужного json файла с результатами
pattern = 'allure-results/*-result.json'
result_files = glob.glob(pattern)

if not result_files:
    print("Нет найденных файлов.")
else:
    # Поиск нового файла
    latest_file = max(result_files, key=os.path.getmtime)

    with open(latest_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Преобразование данных в текстовый формат
    # Преобразование дат из Unix в московское время
    start_data = data['start']
    end_data = data['stop']

    # Начало текста в московское время
    moscow_time_start = pendulum.from_timestamp(start_data / 1000, tz='UTC').in_tz('Europe/Moscow')

    # Окончание
    moscow_time_end = pendulum.from_timestamp(end_data / 1000, tz='UTC').in_tz('Europe/Moscow')

    result_text = f"""
Тестирование отправки формы для практикума
---------------------------------------------
Статус: {data.get('status', 'неизвестно')}
Описание: Тест проверяет функциональность отправки формы на сайте practice-automation.com

Время начала: {moscow_time_start}
Время окончания: {moscow_time_end}
UUID: {data['uuid']}
History ID: {data['historyId']}
Test Case ID: {data['testCaseId']}
Полное имя: {data['fullName']}
Шаги теста: 
"""

    for step in data.get('steps', []):
        step_start = step['start']  # Получаем время начала шага
        step_end = step['stop']  # Получаем время окончания шага

        # Преобразуем время начала и окончания шага в московское время
        moscow_time_step_start = pendulum.from_timestamp(step_start / 1000, tz='UTC').in_tz('Europe/Moscow')
        moscow_time_step_end = pendulum.from_timestamp(step_end / 1000, tz='UTC').in_tz('Europe/Moscow')

        result_text += f"- {step['name']}: {step['status']} (начало: {moscow_time_step_start}, конец: {moscow_time_step_end})\n"

    if data.get('attachments'):
        result_text += "\nПриложения:\n"
        for attachment in data['attachments']:
            result_text += f"- {attachment['name']} (тип: {attachment['type']}, источник: {attachment['source']})\n"

    # Сохранение данных в текстовый файл
    with open('tests/Результаты_теста.txt', 'w', encoding='utf-8') as file:
        file.write(result_text.strip())

    print("Отчет создан!")