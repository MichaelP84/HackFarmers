import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

loaded_model = pickle.load(open('knnpickle_file', 'rb'))

def predict(x):
 return loaded_model.predict(x)

N = input('What is N?')
P = input('What is P?')
K = input('What is K?')
temperature = input('What is temp?')
humidity = input('What is humidity?')
pH = input('What is pH?')
rainfall = input('What is rainfall?')

x = [N, P, K, temperature, humidity, pH, rainfall]
x = np.array(x, dtype=float)
print( predict([x]) )