import numpy as np
from PIL import Image

# img=np.array(Image.open('cat.jpg'))     #картинку в массив
# print(img[0,0])
# imgR = img.copy()
# imgR[:,:,(1,2)]=0
# '''
# 0-это красный
# 1 - зеленый
# 2 - синий
# '''
# img1 = Image.fromarray(imgR)
# img1.save('R.png',format='PNG')
#
# imgG = img.copy()
# imgG[:,:,(0,2)]=0
# img1 = Image.fromarray(imgG)           #массив в картинку
# img1.save('G.png',format='PNG')
#
# imgF = img.copy()
# imgF[:,:,(1)]=0
# img1 = Image.fromarray(imgF)           #массив в картинку
# img1.save('F.png',format='PNG')
#
# imgGRAY = img.copy()
# imgGRAYnew=np.mean(imgGRAY, axis=2).astype(np.uint8)
# print(imgGRAYnew[0,0])
# img1 = Image.fromarray(imgGRAYnew)
# img1.save('gray.png',format='PNG')
#
#
#
# imgGB = np.array(img)
#
# # Зеленый
# imgGB[:100, :, (0, 2)] = 0
#
# # Фиолетовый
# imgGB[100:200, :, (0, 1)] = 0
#
# # Серый
# imgGB[200:300, :] = np.mean(imgGB[200:300, :], axis=-1, keepdims=True)
#
# # Красный
# imgGB[300:, :400, (1, 2)] = 0


# img1 = Image.fromarray(imgGB.astype('uint8'))
# img1.save('GB.png', format='PNG')

img2 = np.array(Image.open('cat1.jpg'))
imgHW = img2.copy()

# Зеленый
imgHW[:100, :100, (1, 2)] = 0

# Фиолетовый
imgHW[:100, :200, (0, 1)] = 0
#
# Серый
imgHW[200:100, :, :] = np.mean(imgHW[200:300, :, :], axis=-1, keepdims=True).astype(int)#
# Красный
imgHW[100:, :100, (1, 2)] = 0

img2 = Image.fromarray(imgHW.astype('uint8'))
img2.save('HW.png', format='PNG')