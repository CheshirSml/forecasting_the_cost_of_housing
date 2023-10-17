from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import json

# загружаем модель из файла
with open('model/best_cb_model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg


@app.route('/predict', methods=['POST'])
def predict_func():
	features = request.json
	columns = ['status', 'propertyType', 'baths',
                'fireplace', 'city', 'sqft', 'zipcode',
                'state', 'PrivatePool', 'Year built', 'Heating',
                'Cooling', 'Parking', 'school_rating _mean', 'school_dist_min']
 
	features_f = pd.DataFrame([features], columns=columns)
	
	predict = model.predict(features_f)
	return jsonify({'prediction': round(np.exp(predict[0]))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)