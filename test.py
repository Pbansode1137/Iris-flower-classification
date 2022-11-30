

#with open(path, 'rb') as file:
#    pickle.load
import numpy as np
import pickle

Iris_model = pickle.load(open("Iris_model.pickle","rb"))

def predict_species(SepalLengthCm,SepalWidthCm, PetalLengthCm, PetalWidthCm):
    x = np.zeros(4)
    x[0] = SepalLengthCm
    x[1] = SepalWidthCm
    x[2] = PetalLengthCm
    x[3] = PetalWidthCm
    species= Iris_model.predict([x])[0]
    return species

