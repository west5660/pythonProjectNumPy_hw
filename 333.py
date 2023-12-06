import numpy as np

a = [1,2,3,4,5]
arr  =np.array(a)

arr = np.arange(1,26).reshape(5,5)
print(arr)

print(arr.shape) #форма 5 на 5
print(arr.size)  #размер массива
print(arr.ndim)  #измерение
print(arr.dtype)

arr = np.random.randint(10,99,size=(2,6)) # матрица 2 на 6
print(arr)

arr = arr.reshape(4,3) # 4 na 3
print(arr)
arr = np.resize(arr,new_shape=(2,2,))  #матрица 2 на 2
print(arr)
arr = np.linspace(0,5,num=15)
print(arr)

arr = np.arange(1,10).reshape(3,3)
print(arr)
print(arr*2)
print(arr<4)
newarr=arr[arr<4]
print(newarr)

newarr = arr[(arr<8)&(arr%2==0)] #проверка на и and

print(newarr)
newarr = arr[(arr<8)|(arr%2==0)]   #проверка на или or
print(newarr)
print(arr)
print(arr[1,2])  #коорд цифры 6
print(arr[1:1])  #коорд цифры 1
print(arr[:,1])  #столбик 1
print(arr[1:,0:2])  #вырезаем квабад
print(np.mean(arr,axis=0))
arr = np.delete(arr,1,axis=0)
print(arr)
arr = np.insert(arr,1,values=[0,0,0],axis=0)
print(arr)

ran = np.random.randint(1, 1001, 50)
ar1 = ran.reshape(5, 10)
ar2 = ar1.reshape(10, 5)

max_ar2=np.max(ar2)
min_ar2=np.min(ar2)
mean_ar2=np.mean(ar2)
print('#########################')
print(max_ar2,min_ar2,mean_ar2)

max_str2=np.max(ar2,axis=1)
min_str2=np.min(ar2,axis=1)
mean_str2=np.mean(ar2,axis=1)
print(max_str2,min_str2,mean_str2)