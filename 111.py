import numpy as np

'''
для аналитики
numpy работает с вычислениями высшей математики
pandas - позволяет numpy работать с таблицами
plotly - библиотека для графиков
'''

'''
направления
прикладные вычисления (автоматизация процессов, аналитика больших данных)
серверное программирование (джанго)
работа с ии (нейросети и боты)


'''
a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
c = np.arange(0,10)
print(c)
d = np.random.rand(3,3)
print(d)
z = np.zeros((3,5))
print(z)
e = np.ones((3,5))
print(e)

m1 = np.random.randint(1,9, size=(3,3))
m2 = np.random.randint(1,9, size=(3,3))
print(m1)
print(m2)
print('##########################################')
m3=m1+m2
print(m3)
# m3*=-1
# print(m3)
print('##########################################')
maxM=np.max(m3)
minM=np.min(m3)
sumM=np.sum(m3)
averM=np.average(m3)
print(maxM,minM,sumM,averM)