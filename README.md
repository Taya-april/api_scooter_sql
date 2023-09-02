# Описание
Проект: Автоматизация теста на получение заказа по треку с помощью API Яндекс Самокат
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest

Разработано и протестировано на **Python 3.11**

# Структура проекта и ее описание

- **config.py**: Хранение путей для запросов в проекте

- **data.py**: Данные, используемые в теле запроса

- **create_order_test.py**: Тест создания и получения заказа в БД

- **sending_requests.py**: Содержит функцию создания нового заказа, функццю получения заказа по треку

- **README.md**: Информация и инструкции о проекте и его запуске

- **.gitignore**: Содержит файлы и папки для игнорирования Git

# Запуск проекта
1. Установить библиотеку Pytest `pip install pytest`
2. Установить пакет requests `pip install requests`
2. Задать необходимые тестовые данные в файле `data.py` и `configuration.py` при необходимости
3. Запуск теста выполнить из терминала PyCharm командой `pytest` 