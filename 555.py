import numpy as np

data = np.genfromtxt('litecoin.csv', delimiter=',', skip_header=1, usecols=(1,4))
maximus = np.max(data, axis=0)
numbers = np.argmax(data, axis=0)

import pandas as pd

newdata = pd.read_csv('litecoin.csv')
print(newdata)
print(newdata.describe())
aaa = newdata['Date']

print('в первой колонке макс', numbers[0], aaa[numbers[0]], 'равен', maximus[0])
print('в первой колонке макс', numbers[1], aaa[numbers[1]], 'равен', maximus[1])