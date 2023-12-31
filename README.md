>## :briefcase: Итоговый проект по автоматизации тестирования SKILLFACTORY QAP-1035
Тест кейсы находятся тут https://docs.google.com/spreadsheets/d/1_OZHGdic5V9LOWBJMtBD6MTK_wjBK7G1tbjGPybVjRE/edit#gid=0

Баг репорты тут https://docs.google.com/spreadsheets/d/1W4MF99YiLG2x90jC0hO_ci4plQ4Lg5TafVb4gPHbznQ/edit#gid=0
### Необходимо протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком.

→ Объект тестирования: https://b2c.passport.rt.ru


→ [Требования по проекту (.doc)](https://docs.google.com/document/d/12yoTwHSTXxIUQQCH32OvlSd3QYUt_aQk/edit)


**:bookmark_tabs: Заказчик передал вам следующее задание:**

1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

**:bookmark_tabs: Ожидаемый результат**

1. Перечислены инструменты, которые применялись для тестирования.

   * Почему именно этот инструмент и эту технику.
   * Что им проверялось.
   * Что именно в нем сделано.
   
2. К выполненному заданию прикреплены:

   * Набор тест-кейсов;
   * Набор автотестов на GitHub.
   * Описание оформленных дефектов.

***
**В корневом каталоге проекта содержится:**
* conftest.py условия для выполнения тестов.
* pytest.ini содержит указание на автоматическую генерацию html-отчета.
* README.mdсодержит информацию в целом о проекте.
* requirements.txt содержит все библиотеки и зависимости проекта.
***
**Директория pages содержит все общие методы и утилиты для всех страниц, методы и утилиты для страницы авторизации.**
***
**:bookmark_tabs: Директория tests содержит CSS-стили для html-отчёта, базовый тестовый класс, автотесты для страницы авторизации.
***
**Директория utilities содержит локаторы страницы, данные для проверок авторизации.**
***


### При разработке тест-кейсов были применены следующие техники тест-дизайна: 
 
* эквивалентное разбиение
* анализ граничных значений
* предугадывание ошибок


### Инструменты, которые применялись для тестирования.

* Для тестирования сайта был использован 
интсрумент Selenium
* Специальный тестовый фреймворк Pytest
* Плагин для pytest, который генерирует HTML-отчет по результатам тестов 
* Для определения локаторов использовались 
следующие инструменты: DevTools, ChroPath.

### Запуск тестов:
* установить все библиотеки и зависимости: `pip install -r requirements.txt`.
* убедитесь что у вас присутствуют основные браузеры для тестирования - в файле conftest.py у фикстуры initialize_driver можете изменить браузер.
* запустить тесты: `pytest tests/test_auth.py`.
* запустить один тест: `pytest tests/test_auth.py::TestAuth::название_нужного_теста`.


