from flask import request, Flask

from ml_model import get_model_prediction


app = Flask(__name__)

model_name = 'catboost_model'
version = '0.1'


host = '0.0.0.0'


@app.route('/info', methods=['GET'])
def info():

    """Return model meta information"""

    result = dict()

    result['model_name'] = model_name
    result['version'] = version

    return result


@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()

    if not json_data:
        return {
            'error': 'No input data received'
        }, 500

    try:
        response = get_model_prediction(json_data)
    except Exception as e:
        return {
            'error': f'Internal error: {str(e)}'
        }, 500

    return response


if __name__ == '__main__':
    app.run(host)
