from flask import Flask, render_template, request
import pandas 
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("Loan(Y,N).pkl", 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():

    temp_array=[]

    Property_area = request.form["Property_Area"]
    if Property_area == 'Property_Area_Semiurban':
        temp_array = temp_array + [1,0]
    elif Property_area == "Property_Area_Urban":
        temp_array = temp_array + [0,1]

    features = [float(x) for x in request.form.values()]
    final_features = features + temp_array
    data = np.array([final_features])

    my_prediction = int(model.predict()[0])
    return render_template('index.html', prediction_text='You Are Eligible: {}'.format(my_prediction))

    