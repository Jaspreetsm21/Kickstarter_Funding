import flask
from flask import Flask, jsonify, request
import json
from data_input1 import data
import numpy as np
import pickle
import pandas as pd
from waitress import serve


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():

    #data
    X = np.array(data_in2).reshape(1,-1)
    print(X)
    #load model
    model = load_models()
    prediction = model.predict(X)[0]
    
    response = json.dumps({'response': float(prediction)})
    return response, 200


if __name__ == '__main__':
    app.run(port = 5000, debug=True)
      # serve(app, host='0.0.0.0', port=5000)


