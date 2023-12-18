import pandas as pd

dframe = pd.read_csv('students.csv')
sred = dframe[['Математика','Физика','Химия','Информатика','История']].mean(axis=1).round(2)
dframe['Средний']=sred
print(sred)
dframe = dframe.sort_values('Средний', ascending=False)

dframe.to_excel('exel.xlsx', index=False)   #сохранили новый ексель файл

print(dframe['Средний'].max())
print(dframe['Средний'].idxmax())
maxball = dframe['Средний'].max()
newf = dframe[dframe['Средний']==maxball]  #фильтр по количеству максимального балла
print(newf['Имя'])
minball = dframe['Средний'].min()
newf1 = dframe[dframe['Средний']==minball]
print(newf1['Имя'])

