import numpy as np

years = np.random.randint(2010,2024,size=(100000,1))
sales = np.random.randint(500,1500, size=(100000,1))
viruchka = np.random.randint(50000,150000,size=(100000,1))

data = np.concatenate((years,sales,viruchka), axis=1)
newdata = data[data[:,0]==2018]
sum18sales = np.sum(newdata[:,1])
sum18vir = np.sum(newdata[:,2])

import pandas as pd
df=pd.DataFrame(data)
print(df)
print(df.columns)
df2=df.groupby(0).sum()
print(df2[1].max())
print(df2[2].max())
maximus = df2.idxmax(axis="index")
print('больше продаж в ', maximus[1] )
print('больше выручка в ', maximus[2] )


years_new, counts = np.unique(data[:, 0], return_counts=True)
#находим уникальные значения и их кличество в первом столбце data
 #в результате получим два массива

sum_sales = np.bincount(data[:, 0], weights=data[:, 1], minlength=2014-2010+1)[2010:]
#считаем суммы продаж в каждом году. weights=data[:, 1] - берем значения из второго столбика
#minlength задает минимальную длину результата.
sum_viruchka = np.bincount(data[:, 0], weights=data[:, 2], minlength=2014-2010+1)[2010:]
#считаем суммы продаж в каждом году. weights=data[:, 1] - берем значения из третьего столбика
#minlength задает минимальную длину результата.

max_sales_year = years_new[np.argmax(sum_sales)]
#Находим год с максимальной суммой продаж, используя индекс максимального значения
# из sum_sales и соответствующий год из years_new.
max_viruchka_year = years_new[np.argmax(sum_viruchka)]  #находим выручку

print('###################################################################')
print('Больше продаж в', max_sales_year, 'году, сумма:', np.max(sum_sales))
print('Больше выручки в', max_viruchka_year, 'году, сумма:', np.max(sum_viruchka))