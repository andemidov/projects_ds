import datetime as dt

from catboost import CatBoostRegressor

model = CatBoostRegressor()
model.load_model('/home/yuriy/YandexPracticum/Workshop8/catboost_model')


wall_types = ['None', 'block', 'brick', 'monolith', 'monolithBrick', 'old',
       'panel', 'stalin', 'wood']

wall_type_mapping = dict(zip(wall_types, range(len(wall_types))))


def get_model_prediction(json_data):
    start = dt.datetime.now()

    walls_material = json_data.get('wallsMaterial', 'unknown')
    floor_number = json_data.get('floorNumber', 6)
    floors_total = json_data.get('floorsNumber', 14)
    total_area = json_data.get('totalArea', 59)
    kitchen_area = json_data.get('kitchenArea', 10)
    distance_to_center = json_data.get('distance_to_center', 16.27)

    walls_material_encoded = wall_type_mapping.get(walls_material, -1)

    X = [[floor_number, floors_total, total_area, kitchen_area, distance_to_center, walls_material_encoded]]

    price_prediction = model.predict(X)

    return {
        'status': 200,
        'price_estimation': int(price_prediction),
        'duration': (dt.datetime.now() - start).total_seconds(),
    }



