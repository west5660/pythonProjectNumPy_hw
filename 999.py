import pandas as pd

dframe = pd.read_excel('movies.xlsx')
drama = dframe[dframe['Жанр'] == 'драма']
spielberg = dframe[dframe['Режиссер'] == 'Стивен Спилберг']
rating = dframe['Рейтинг'].max()
top_rating = dframe[dframe['Рейтинг'] == rating]
year = dframe[dframe['Год'] >= 2005]
print('########################################### Драмма')
print(drama)
print('########################################### Спилберг')
print(spielberg)
print('########################################### Рейтинг')
print(top_rating)
print('########################################### С 2005 года')
print(year)
print('########################################### еще задание')


