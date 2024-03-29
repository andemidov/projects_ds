# Определение стоимости автомобилей

## Основные навыки: Python, Pandas, lightgbm, catboost

Сервис по продаже автомобилей с пробегом «Не бит, не крашен» разрабатывает приложение для привлечения новых клиентов. В нём можно быстро узнать рыночную стоимость своего автомобиля. В вашем распоряжении исторические данные: технические характеристики, комплектации и цены автомобилей. Вам нужно построить модель для определения стоимости. 

Заказчику важны:

- качество предсказания;
- скорость предсказания;
- время обучения.

**Описание целей и задачи проекта**

Сервис по продаже автомобилей с пробегом «Не бит, не крашен» разрабатывает приложение для привлечения новых клиентов. В нём можно быстро узнать рыночную стоимость своего автомобиля. Необходимо построить модель для определения стоимости.

Заказчику важны:

- качество предсказания
- скорость предсказания
- время обучения

**Описание данных**

Таблица с историческими данными: технические характеристики, комплектации и цены автомобилей.
Признаки:
- DateCrawled — дата скачивания анкеты из базы
- VehicleType — тип автомобильного кузова
- RegistrationYear — год регистрации автомобиля
- Gearbox — тип коробки передач
- Power — мощность (л. с.)
- Model — модель автомобиля
- Kilometer — пробег (км)
- RegistrationMonth — месяц регистрации автомобиля
- FuelType — тип топлива
- Brand — марка автомобиля
- NotRepaired — была машина в ремонте или нет
- DateCreated — дата создания анкеты
- NumberOfPictures — количество фотографий автомобиля
- PostalCode — почтовый индекс владельца анкеты (пользователя)
- LastSeen — дата последней активности пользователя

Целевой признак:
- Price — цена (евро)

**План работы**

- загрузить и познакомиться с данными
- изучить данные, заполнить пропущенные значения и обработать аномалии в столбцах (если среди признаков имеются неинформативные - удалить)
- подготовить выборки для обучения моделей
- обучить разные модели, одна из которых — LightGBM, как минимум одна — не бустинг (для каждой модели попробоваьб разные гиперпараметры)
- проанализировать время обучения, время предсказания и качество моделей
- опираясь на критерии заказчика, выбрать лучшую модель, проверить её качество на тестовой выборке
    
    Примечания:
    для оценки качества моделей применить метрику RMSE.
    Значение метрики RMSE должно быть меньше 2500.

## Выводы

Итогом данной работы будет модель, которая позволит пользователям определиться с рыночной ценой машины. В случае с продажей, клиенты смогут получить оценку рыночной стоимости для выставления адекватной цены. В случае с приобретением автомобиля, пользователи смогу понять на какие машины можно обратить внимание исходя из бюджета. Так же эта функция повысит интерес к сервису и увеличит приток клиентов.


Посторены и обучены три модели:

Модель CatBoostRegressor показала себя хорошо, MRSE = 1688. Лучшие параметры 'depth': 10, 'l2_leaf_reg': 1, 'learning_rate': 0.1
Обучение занимает 0.114 мин. Предсказание занимает 0.0005 мин.

Модель LightGBM показала себя так же хорошо, MRSE = 1830. Лучшие параметры 'learning_rate': 0.1, 'max_depth': 5, 'num_leaves': 10
Обучение занимает 2.029 мин. Предсказание занимает 0.0065 мин.

Модель Ridge показала хуже свех, MRSE = 2612. Лучшие параметры: 'alpha': 0.1, 'solver': 'svd'
Обучение занимает 1.01 мин. Предсказание занимает 0.0036 мин.

MRSE CatBoostRegressor на тестовой выборке 1707, это соответсвует условиям задачи. Модель прошла проверку на адекватность. На обучение потребовалось 0.114 сек. На предсказание 0.0005 мин.
