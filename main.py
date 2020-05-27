import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math

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


def getMedia(image):
    media = 0    
    for x in np.nditer(image):
        media += x
    media = media/(image.shape[0]*image.shape[1])
    return media


def getDesvio(imagen, media):
    desvio = 0
    for x in np.nditer(imagen):
            desvio = desvio + ((x - media)**2)
    desvio = desvio/(imagen.shape[0]*imagen.shape[1])
    return math.sqrt(desvio)

def getCorrelacionCruzada(imagenA, imagenB, mediaA, mediaB):
    sxy = 0
    for (x,y) in zip(np.nditer(imagenA),np.nditer(imagenB)):
        sxy = sxy + ((x - mediaA) * (y - mediaB))
    sxy = sxy/(imagenA.shape[0]*imagenA.shape[1])
    return sxy

def getFactorCorrelacion(imagenA, imagenB):
    mediaA = np.mean(imagenA)
    mediaB = np.mean(imagenB)
    desvioA = np.std(imagenA)
    desvioB =  np.std(imagenB)
    sxy = getCorrelacionCruzada(imagenA, imagenB, mediaA, mediaB)
    return sxy/(desvioA*desvioB)

# res = cv.matchTemplate(imgWill1,imgWillOriginal,cv.TM_CCOEFF_NORMED)
# print(res)
r = getFactorCorrelacion(imgWill1[:,:,0], imgWillOriginal[:,:,0])
print("Image 1")
print(r)
r = getFactorCorrelacion(imgWill2[:,:,0], imgWillOriginal[:,:,0])
print("Image 2")
print(r)
r = getFactorCorrelacion(imgWill3[:,:,0], imgWillOriginal[:,:,0])
print("Image 3")
print(r)
r = getFactorCorrelacion(imgWill4[:,:,0], imgWillOriginal[:,:,0])
print("Image 4")
print(r)
r = getFactorCorrelacion(imgWill4[:,:,0], imgWillOriginal[:,:,0])
print("Image 5")
print(r)