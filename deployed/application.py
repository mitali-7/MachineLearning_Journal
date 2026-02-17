from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


application = Flask(__name__)
app = application

ridge_model = pickle.load(open('ridge.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


@app.route("/")
def index():
    return redirect(url_for('predict'))
    # return render_template('home.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)
        return render_template("home.html", results = result[0])
    
    else:
        return render_template("home.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run(debug=True, port=5001)

