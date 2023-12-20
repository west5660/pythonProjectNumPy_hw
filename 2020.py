
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go

dframe = pd.read_csv('sales_data.csv')
sales = dframe.groupby('Магазин').size().reset_index(name='Количество продаж')
# fig = px.pie(sales, values='Количество продаж', names='Магазин', title='Продажи по магазинам')
# fig.show()

# Сгруппируем данные по товарам и количеству продаж для каждого магазина
product_sales = dframe.groupby(['Магазин', 'Фрукт']).size().reset_index(name='Количество продаж')

# Создаем гистограмму
fig = px.bar(product_sales, x='Фрукт', y='Количество продаж', color='Магазин',
                 title='Количество продаж товаров в каждом магазине', barmode='group')
# fig.show()
selected_shop_data = dframe[dframe['Магазин'] == 'Фермер']

# Создаем линейный график
fig = px.line(selected_shop_data, x='Фрукт', y='Цена', color='Фрукт', title='Цены на товары в магазине "Фермер"')
fig.show()