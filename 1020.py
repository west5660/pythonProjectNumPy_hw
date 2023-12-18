import pandas as pd

data = pd.read_csv('sales_data.csv')
print(len(data))
# df=data.Количество
# print(df.to_list())
# ser=pd.Series(df.to_list(),index=pd.date_range(start='2019-01-01', periods=len(df.to_list()),freq='D'))
# print(ser)
ser22 = data.Количество.tolist()
ser33 = data.Дата.tolist()
ser = pd.Series(ser22, index=pd.date_range(start='2022-01-01', periods=len(data)))
# ser = pd.Series(data.Количесто.values, index=pd.date_range(start='2022-01-01' ,periods=len(data)))
print(data)
print(data.head(3))
print(data.tail(4))