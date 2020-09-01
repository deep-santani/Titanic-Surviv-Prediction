# -*- coding: utf-8 -*-
"""
Created on Mon Aug  10 08:31:22 2020

@author: deep
"""

from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Pclass= int(request.form['Pclass'])    
        Age=int(request.form['Age'])
        SibSp=int(request.form['SibSp'])	
        Parch=int(request.form['Parch'])
        Fare=int(request.form['Fare'])
        male=int(request.form['male'])
		
        my_prediction = model.predict([[Pclass, Age ,SibSp ,Parch ,Fare ,male]])
        
        if(my_prediction==[1]):
            my_prediction="Whoooo!!!!!  The Person Will Surviv" 
        else:
            my_prediction="No The Person Will not Surviv"
        return render_template('index.html',prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)