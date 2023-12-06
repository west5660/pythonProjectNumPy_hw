import numpy as np

virushka = np.array([[1000000, 2000000, 2500000, 3000000, 2150000],
                    [1560000, 2330000, 2500000, 3990000, 2150000],
                    [2120000, 2500000, 3770000, 2650000, 4000000],
                    [2589000, 2990000, 4488000, 4586000, 3500000],
                    [2100000, 2599000, 3100000, 2110000, 4233000],
                    [1533000, 2660000, 4220000, 3500000, 2577000]])

cities = np.array(['Нижний Новгород', 'Астрахань', 'Самара', 'Москва', 'Воронеж', 'Санкт-Петербург'])
datas = np.array(['10.07.23', '11.07.23', '12.07.23', '13.07.23', '14.07.23'])

sumSTR=np.sum(virushka,axis=1)  # сумма продаж в городе
sumSTR= sumSTR.reshape(6,1)     #развернули строку вертикально

maxGorod = np.argmax(sumSTR)    #номер максимального числа

print(sumSTR)
print(maxGorod)
print(cities[maxGorod])

print('##########################')
sumCOL=np.sum(virushka,axis=0)
maxData = np.argmax(sumCOL)

print(sumCOL)
print(maxData)
print(datas[maxData])

newT=virushka.T   #повернуть матрицу на 90 градусов
print(newT)
print('##########################')
meanSTR = np.mean(virushka,axis=1)
meanGorod = np.argmax(meanSTR)
print(meanSTR)
print(meanGorod)
print(cities[meanGorod])

meanCOL = np.mean(virushka,axis=0)
meanData = np.argmax(meanCOL)
print(meanCOL)
print(meanData)
print(datas[meanData])

print('##########################')

 # Январь, Февраль, Март, Апрель, Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь, Декабрь
virushka1 = np.array ([[1000, 1200, 1500, 1350, 1400, 1300, 1250, 1450, 1300, 1550, 1600, 1700], # Завод 1
    [800, 900, 1000, 950, 1000, 1100, 1200, 1150, 1000, 1100, 1200, 1300], # Завод 2
    [1200, 1300, 1250, 1400, 1500, 1600, 1650, 1700, 1600, 1550, 1500, 1400], # Завод 3
    [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]]) # Завод 4
zavod = np.array(['Завод 1','Завод 2','Завод 3','Завод 4'])
mouth = np.array(['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'])

sum_tot = np.sum(virushka1)

sum_str = np.sum(virushka1,axis=1)
sum_str= sum_str.reshape(4,1)

product_tot = np.sum(virushka1, axis=1)
product_zavod = np.argmax(product_tot)

mouth_tot = np.sum(virushka1, axis=0)
mouth_zavod = np.argmax(mouth_tot)

print('Всего выпущенно велосипедов : ',sum_tot,' тысяч штук')
for i, sum_str_vivod in enumerate(sum_str):
    print(f'Сумма выпущенных изделий за год на Заводе {i + 1}: {sum_str_vivod[0]} тысяч штук')
print('Самый продуктывный выпуск : ', zavod[product_zavod])
print('Самый продуктывный месяц : ', mouth[mouth_zavod])
# Напишите программу, которая определит:
#
# Общее количество выпущенных велосипедов.
# Количество велосипедов, произведенных на каждом заводе за год.
# Самый продуктивный завод компании.
# Самый продуктивный месяц компании.