
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go

# dx = [1,2,3,4]
# dy = [1,4,9,16]
# fig = px.line(x = dx, y = dy, title = 'Grafik')
# fig.show()

# dx = np.arange(0,10,0.5)
# def f1(x):
#     return x*x

# fig = px.bar(x = dx, y = f1(dx), title='Grafik')
# fig.show()

'''
line,
scatter,
area,
bar,
line
'''

# dframe = px.data.carshare()
# # fig = px.bar(dframe, x = 'peak_hour', y='car_hours')
# dsum=dframe.groupby(dframe.peak_hour).sum()
# fig = px.bar(dsum, y = 'car_hours', x = dsum.index, color='car_hours',
#              color_continuous_scale=['red','orange','green','blue','violet'])
# fig.show()

dframe = pd.read_excel('exel.xlsx')
fig = px.funnel(dframe, x = dframe.index, y = dframe.Средний)
# fig.show()
dframe = px.data.election()
dsum = dframe.groupby(dframe.winner).count()
fig = px.pie(dsum, names=dsum.index, values=dsum.result)
# fig.show()

data2 = [100000, 120000, 150000, 80000, 200000, 250000, 180000, 300000, 280000, 320000, 350000, 400000,
        180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000,
        150000, 300000, 250000, 280000, 320000, 350000, 380000, 400000, 420000, 440000, 470000, 500000,
        200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000, 420000,
        150000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000]

ser2 = pd.Series(data2, index=pd.date_range(start='2019-01-01', periods=len(data2), freq='M', name='name'))
fig = px.line(ser2, x = ser2.index, y = data2)
# fig.show()

dx = np.arange(1,100)   #ось ч от 1 до 100
dy= np.random.randint(1,10, size=100)
dy2= np.random.randint(20,50, size=100)
dy3= np.random.randint(60,100, size=100)

fig= go.Figure()        #пустой график
graf1 = go.Scatter(x=dx,y=dy, name = 'gra'
                                     'f1', mode='markers')   #создается одна линия
graf2 = go.Scatter(x=dx,y=dy2, name = 'graf2', mode='markers+lines')
graf3 = go.Scatter(x=dx,y=dy3, name = 'graf3', mode='lines')
fig.add_trace(graf1)   #добавляется на график
fig.add_trace(graf2)
fig.add_trace(graf3)
# fig.update_layout(xaxis='точки',yaxis='от 1 до 100', title = 'График')
#подписи графика
fig.update_layout(title = 'Графика')
fig.update_xaxes(title='Точки')
fig.update_yaxes(title = 'От 1 до 100')
fig.show()   #нарисовать график