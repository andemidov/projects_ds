# Отток клиентов

## Основные навыки: Pandas, Matplotlib, Scikit-learn

**Описание целей и задачи проекта**

Из «Бета-Банка» стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых.
Задача спрогнозировать, уйдёт клиент из банка в ближайшее время или нет.

**Описание данных**

В распряжении есть исторические данные о поведении клиентов и расторжении договоров с банком. Каждая строчка содержит информацию об одном клиенте.

**План работы**

Необходимо построить модель с предельно большим значением *F1*-меры. Проверьить *F1*-меру на тестовой выборке и довести метрику до 0.59. Так же измерить *AUC-ROC* и сравнить её значение с *F1*-мерой.
Для этого мы сделаем:
- изучение и предобработку данных
- сделваем из данных обучающую, валидационную и тестовую выборки
- преобразуем данные для обучения моделей
- обучим три модели алгоритмов:
    - дерево решений
    - случайный лес
    - логистическая регрессия
- подберём необходимые паметры и гиперпараметры
- проверим модель на адекватность

## Выводы

Результатом работы будет модель, которая предскажет какой клиент, возможно, уйдёт. С этим клиентом можно дополнительно поработать: узнать чем он недоволен, предложить допуслуги или выгодные предложения, это уменьшит уход клиентов - поможет сохранить или преумножить доходы компании, а так же лучше знать потребности своих клиентов.

В работе разобрано три алгоритма (дерево решений, случайный лес и логистическая регрессия). Логистическая регрессия не подходит для данной задачи, т к показатели качества у неё низкие и ингда даже как у случайной модели. Дерево решений показывает лучший результат и на валидационной выборке показала результаты F1 = 0,59 и AUC-ROC = 0,81. Я исследовал порог классификации и выяснил, что значение его имеет лучшие результатыт на уровне 0.34.

На тестовой выборке F1 = 0.54, AOC-ROC = 0.74. Такой результат соответствуют заданию и модель прошла проверку на адекватность. Но показатель AUC-ROC уменьшился.
