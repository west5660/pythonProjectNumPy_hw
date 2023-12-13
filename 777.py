import pandas as pd

data={'Name':['Boris','Max','Tomas','Robert'],
      'Age':[25,35,45,55],
      'City':['NY','LA','SPB','Sochi'],

}
dframe = pd.DataFrame(data)   #преобразует данные в таблицу
# dframe = dframe.rename(columns={})
dframe.columns=['A','B','C']   #переименовать колонки
dframe.index=['a','b','c','d'] #переименовать строки
print(dframe.loc['a','A'])    #достать данные по названию колонок и строк
print(dframe.iloc[0,0])       # достать данные по номеру колонок и строк
print(dframe.loc['a'])        # строка
print(dframe.loc[:,'A'])      #столбец

import numpy as np
arr = np.random.randint(10,99, size=(4,4))
arrframe = pd.DataFrame(arr)    # создали таблицу из нумпи
arrframe.columns = ['A','B','C','D']

dframe = pd.read_csv('data.csv')   # открыли файл
dsort2 = dframe.sort_values(by='столбец_2')  #сортировка
dsort3 = dframe.sort_values(by='столбец_3')

dframe = dframe.drop(['столбец_1'], axis=1)   #удалили столбец_1

data = {'Name':['Igor','Anna','Igor','Anna','Zahar'],
        'Money':[120,130,140,105,160]

}

dframe = pd.DataFrame(data)
newframe = dframe.groupby(by='Name').sum()  #группировка по имени + сложение повторяющихся ячеек

print('################################')
data1={'Name':['Boris','Max','Tomas','Robert','Alex','Sergey','Alisa','Vera','Olga','Sofia'],
      'Rost':[165,135,145,155,202,200,182,171,165,185],
      'Massa':[60,78,89,69,102,121,89,74,63,55],

}
ddframe = pd.DataFrame(data1)
dsort4 = ddframe.sort_values(by='Rost')
print(ddframe.iloc[1])       # достать данные по номеру колонок и строк
print(ddframe.iloc[3])       # достать данные по номеру колонок и строк
print(ddframe.iloc[5])       # достать данные по номеру колонок и строк