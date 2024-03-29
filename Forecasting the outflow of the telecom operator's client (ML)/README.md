# Прогнозирование оттока клиента оператора связи

## Основные навыки: Python, Pandas, lightgbm, catboost, Scikit-learn

**Описание целей и задачи проекта**

Заказчик оператор связи «Ниединогоразрыва.ком» хочет научиться прогнозировать отток клиентов. Необходимо создать классифицирующую модель, предсказывающую вероятнотность того, что клиент планирует уйти или остаться. 

**Описание данных**

В распоряжении информация о договорах актуальных на 1 февраля 2020. Данные представлены в 4 таблицах:

Таблица **contract** — информация о договоре:
 - customerID код клиента
 - BeginDate дата, кода клиент начал пользоваться услугами компании
 - EndDate дата, кода клиент закончил пользоваться услугами компании 
 - Type период оплаты
 - PaperlessBilling возможность получения электронного чека
 - PaymentMethod способ оплаты
 - MonthlyCharges стоимость услуг за месяц
 - TotalCharges общая выручка за все услуги с клиента


Таблица **personal** — персональные данные клиента:
 - customerID код клиента
 - gender пол
 - SeniorCitizen пожилой человек (возраст 65+)
 - Partner семейное положение (в браке)
 - Dependents количество детей

Таблица **internet** — информация об интернет-услугах:
 - customerID код клиента
 - InternetService тип подключения интернета
 - OnlineSecurity подключение блокировки небезопасных сайтов
 - OnlineBackup подключение облачного хранилища
 - DeviceProtection подключение интернет-безопасности
 - TechSupport подключение к выделенной линии технической поддержки
 - StreamingTV подключение к стриминговому телевидинию
 - StreamingMovies поключение к каталогу фильмов
 
Таблица **phone** — информация об услугах телефонии:
 - customerID код клиента
 - MultipleLines подключение телефонного аппарата к нескольким линиям одновременно

**План работы**

 - изучение и предобработка данных
     - загрузка и ознакомление
     - приведение к общему "питоновскому стилю"
     - работа с пропусками и дубликатами
     - приведение к нужным типам данных
     - определение целевой переменной
 -  работа с признаками
     - исключение ненужных признаков
     - формирование новых признаков
     - анализ дисбаланса целевого класса
     - объединение таблиц в одну и работа с новыми пропусками
     - проверка корреляции признаков и корреляции с целевым признаком
 - разбивка данных обучающую и тестовую выборки
 - обучить минимум две модели на разных алгоритмах
     - подготовка признаков для каждой модели
     - подборгиперпараметров на кросвалидации
 - AUC-ROC мера на тестовой выборке должна быть не ниже 0.85, так же необходимо посчитать F1 и accuracu
 - тест лучшей модели и проверка на адекватность
 - анализ важности признаков выбранной модели
 - выводы по исследованию
 
## Выводы 
 
 Данное исследование позволит определить, какие параметры влияют на лояльность клиентов. Помогут понять в каких направлениях стоит разработать нововведения. Какие услуги можно предложить клиентам со скидками для их удержания в компании. В результате данной работы получится модель, которая предскажет с какими клиентами необходимо дополнительно взаимодействие, чтобы их сохранить. И как результат сохранить и увеличить прибыль компании.
 
 Построенная модель предсказывает уход клиента с вероятностью 86%. Модель заметно отличается от случайной модели в лучшую сторону, а главная метрика на тесте даже немного увеличилась AUC-ROC = 0.9. Соотношение точности и полноты 70%. Самым важным признаком получился созданный признак "количество дней, которое клиент был активным", что логично: чем больше клиент в компании, тем он лояльнее. Далее идёт признак "тип оплаты" - если клиент оплачивает сразу год, он не думает в ближайшее время уходить. Далее следую признаки, связанные со стоимостью услуг за месяц, и общая выручка за все услуги с клиента. Всё это указывает на то, что показатели, связанные с продолжительностью сотрудничества и деньгами, говорят о лояльности клиентов. Возможно предложить клиентам промокоды на оплату за год, полгода или оплату допуслуг, тк если клиент начинает платить больше - вероятность его ухода снижается.
