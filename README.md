# Sst
SimbirSoft test

Тест-кейсы:

Позитивный

    Тест проверяет корректное заполнение формы на сайте
    
    Шаги:
        1. Запустить браузер, перейти на страницу "https://practice-automation.com/form-fields/"
        2. Заполнить поле "Name" значением "Yury"
        3. Заполнить поле "Password" значением "12345"
        4. Отметить варианты "Milk" и "Coffee" в разделе "What is your favorite drink?"
        5. Отметить вариант "Yellow" в разделе "What is your favorite color?"
        6. Выбрать вариант "Yes" в выпадающем списке "Do you like automation?"
        7. Заполнить поле "Email" значением "name@example.com"
        8. Заполнить многострочное текстовое поле "Message" значением "5 Katalon Studio"
        9. Нажать кнопку "Submit"
    

    Ожидаемый результат:
    1. Появится alert с сообщением "Message received!"
    
Негативный
    
    Тест проверяет заполнение обязательных полей формы на сайте 
    
    Шаги:
        1. Запустить браузер, перейти на страницу "https://practice-automation.com/form-fields/"
        2. Не заполнять поле "Name"
        3. Заполнить поле "Password" значением "12345"
        4. Отметить варианты "Milk" и "Coffee" в разделе "What is your favorite drink?"
        5. Отметить вариант "Yellow" в разделе "What is your favorite color?"
        6. Выбрать вариант "Yes" в выпадающем списке "Do you like automation?"
        7. Заполнить поле "Email" значением "name@example.com"
        8. Заполнить многострочное текстовое поле "Message" значением "5 Katalon Studio"
        9. Нажать кнопку "Submit"
        
    Ожидаемый результат:
    1. Alert с сообщением "Message received!" не появляется
    

