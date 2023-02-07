import os
import pandas as pd
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request


app = Flask(_name_)

@app.route('/')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    loaded_model = pickle.load(open("TrainData.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/ predict', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction = str(result)
    return render_template("predict.html", prediction=prediction)


if _name_ == "_main_":
    app.run(debug=True)