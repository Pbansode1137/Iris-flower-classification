from flask import Flask, request
app = Flask(__name__)

import pandas as pd
import numpy as np
import pickle
import test

@app.route('/predict_species', methods = ['GET','POST'])
def prediction():
    data = request.form
    if request.method == 'GET':
        SepalLengthCm = float(data['SepalLengthCm'])
        SepalWidthCm  = float(data['SepalWidthCm'])
        PetalLengthCm = float(data['PetalLengthCm'])
        PetalWidthCm  = float(data['PetalWidthCm'])
        print('SepalLengthCm,SepalWidthCm, PetalLengthCm, PetalWidthCm',SepalLengthCm,SepalWidthCm, PetalLengthCm, PetalWidthCm )
        species = test.predict_species(SepalLengthCm,SepalWidthCm, PetalLengthCm, PetalWidthCm)
    return 'Predicted Species is {}'.format(species)


if __name__ == '__main__':
    print('Starting Python Flask Server For Iris Species Prediction.......')
    app.run(debug=True)