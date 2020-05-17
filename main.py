import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgWillOriginal = cv.imread("ImagenesWill/Will(Original).bmp")
imgWill1 = cv.imread("ImagenesWill/Will_1.bmp")
imgWill2 = cv.imread("ImagenesWill/Will_2.bmp")
imgWill3 = cv.imread("ImagenesWill/Will_3.bmp")
imgWill4 = cv.imread("ImagenesWill/Will_4.bmp")
imgWill5 = cv.imread("ImagenesWill/Will_5.bmp")
imgWillCanal2 = cv.imread("ImagenesWill/Will_Canal2.bmp")
imgWillCanal8 = cv.imread("ImagenesWill/Will_Canal8.bmp")
imgWillCanal10 = cv.imread("ImagenesWill/Will_Canal10.bmp")
imgWillEj2 = cv.imread("ImagenesWill/Will_ej2.bmp")

# Genera un arreglo de 256 con la cantidad de veces que aparece ese color en la imagen
def obtener_ocurrencia_pixeles(imagen):
    result = [0] * 256
    for i in imagen:
        for j in i:
            result[j[0]] = result[j[0]] + 1

    return result

#Genera el grafico del histograma de una imagen
def obtener_histograma(imagen):
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv.calcHist([imagen],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    return plt

print(obtener_ocurrencia_pixeles(imgWillOriginal))
print(obtener_ocurrencia_pixeles(imgWill5))

hist = obtener_histograma(imgWillOriginal)
hist.show()

his2 = obtener_histograma(imgWill5)
his2.show()
