import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math
import heapq
import os 
import struct
imgWillOriginal = cv.imread("ImagenesWill/Will(Original).bmp")[:,:,0]
imgWill1 = cv.imread("ImagenesWill/Will_1.bmp")[:,:,0]
imgWill2 = cv.imread("ImagenesWill/Will_2.bmp")[:,:,0]
imgWill3 = cv.imread("ImagenesWill/Will_3.bmp")[:,:,0]
imgWill4 = cv.imread("ImagenesWill/Will_4.bmp")[:,:,0]
imgWill5 = cv.imread("ImagenesWill/Will_5.bmp")[:,:,0]
imgWillCanal2 = cv.imread("ImagenesWill/Will_Canal2.bmp")[:,:,0]
imgWillCanal8 = cv.imread("ImagenesWill/Will_Canal8.bmp")[:,:,0]
imgWillCanal10 = cv.imread("ImagenesWill/Will_Canal10.bmp")[:,:,0]
imgWillEj2 = cv.imread("ImagenesWill/Will_ej2.bmp")[:,:,0]

# Genera un arreglo de 256 con la cantidad de veces que aparece ese color en la imagen
def obtener_ocurrencia_pixeles(imagen):
    result = [0] * 256
    for i in imagen:
        for j in i:
            result[j] = result[j] + 1
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
        print(x)
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
    desvioA = getDesvio(imagenA, mediaA)
    desvioB =  np.std(imagenB)
    sxy = getCorrelacionCruzada(imagenA, imagenB, mediaA, mediaB)
    return sxy/(desvioA*desvioB)

# res = cv.matchTemplate(imgWill1,imgWillOriginal,cv.TM_CCOEFF_NORMED)
# print(res)
# r = getFactorCorrelacion(imgWill1, imgWillOriginal)
# print("Image 1")
# print(r)
# r = getFactorCorrelacion(imgWill2[:,:,0], imgWillOriginal[:,:,0])
# print("Image 2")
# print(r)
# r = getFactorCorrelacion(imgWill3[:,:,0], imgWillOriginal[:,:,0])
# print("Image 3")
# print(r)
# r = getFactorCorrelacion(imgWill4[:,:,0], imgWillOriginal[:,:,0])
# print("Image 4")
# print(r)
# r = getFactorCorrelacion(imgWill4[:,:,0], imgWillOriginal[:,:,0])
# print("Image 5")
# print(r)

h, w = imgWillOriginal.shape
print(h)
print(w)

def makeTree(probs):
    q = []
    for i in range(len(probs)):
        if (probs[i] != 0):
            prob = probs[i]/(h*w)
            heapq.heappush(q,(prob,0,i))

    while len(q) > 1:
        e1 = heapq.heappop(q) # El símbolo menos probable
        e2 = heapq.heappop(q) # El segundo menos probable
        
        # Este nuevo nodo tiene probabilidad e1[0]+e2[0]
        # y profundidad mayor al nuevo nodo
        nw_e = (e1[0]+e2[0],max(e1[1],e2[1])+1,[e1,e2])
        heapq.heappush(q,nw_e)
    return q[0] # Devolvemos el arbol sin la fila


def make_dictionary(tree):
    res = {} # La estructura que vamos a devolver
    search_stack = [] # Pila para DFS
    # El último elemento de la lista es el prefijo!
    search_stack.append(tree+("",)) 
    while len(search_stack) > 0:
        elm = search_stack.pop()
        if type(elm[2]) == list:
            # En este caso, el nodo NO es una hoja del árbol,
            # es decir que tiene nodos hijos
            prefix = elm[-1]
            # El hijo izquierdo tiene "0" en el prefijo
            search_stack.append(elm[2][1]+(prefix+"0",))
            # El hijo derecho tiene "1" en el prefijo
            search_stack.append(elm[2][0]+(prefix+"1",))
            continue
        else:
            # El nodo es una hoja del árbol, así que
            # obtenemos el código completo y lo agregamos
            code = elm[-1]
            res[elm[2]] = code
        pass
    return res

def compress(dic, image):
    res = ''
    it = np.nditer(image)
    for x in it:
        # print(x)
        # print(it.next)
        pixel = int(x)
        # pixel = it[0]
        # print(pixel)
        code = dic[pixel]
        res = res + code
    res = '1' + res
    # Agregamos ceros para que la longitud del resultado
    # sea un múltiplo de 8
    head = (8 - len(res) % 8) * '0'
    res = head + res
    # res = res + (len(res) % 8 * "0")
    # print(len(res))
    return res # Convertimos a entero! (2 porque es base 2)

tree = makeTree(obtener_ocurrencia_pixeles(imgWillOriginal))
# print (tree)
dic = make_dictionary(tree)
print(dic)

lista_de_bits = compress(dic, imgWillOriginal)
# print(len(compressed))
# heapq.heapify()

def compressedtoBytes(compressed):
    lista_bytes = []
    for i in range(0, len(compressed), 8):
        # me quedo con 8 caracteres de la lista de bits
        ocho_bits = compressed[i:i+8]
        n = int(ocho_bits, 2)
        byte = bytes([n])
        lista_bytes.append(byte)
    return lista_bytes

# lista_de_bits = '10011000011110110110100011111111'

lista_de_bytes = compressedtoBytes(lista_de_bits)

def escribirBytesEnArchivo(nombreArchivo, arrBytes):
    with open(nombreArchivo, 'wb') as f:
        for byte in arrBytes:
            f.write(byte)
    f.close()

escribirBytesEnArchivo('mi_archivo.teoinfo', lista_de_bytes)

print('Tamaño de archivo: {} bytes'.format(os.path.getsize('mi_archivo.teoinfo')))


def recuperarBytesEnArchivo(nombreArchivo):
    bytes_recuperados = []
    with open(nombreArchivo, 'rb') as f:
        bytes_leidos = f.read()
        for b in bytes_leidos:
            # Recupero cada byte. Elimino los dos primeros caracteres 0b y completo los 8 digitos con 0
            recuperado = bin(b)[2:].zfill(8)
            bytes_recuperados.append(recuperado)
    f.close()
    return bytes_recuperados

bytesRecuperados = recuperarBytesEnArchivo('mi_archivo.teoinfo')

def recuperarTextoComprimido(arrBinario):
    resultado = ''
    for string in arrBinario:
        resultado = resultado + string
    return resultado

# Este comprimidoRecuperado es igual a lista_de_bits
comprimidoRecuperado = recuperarTextoComprimido(bytesRecuperados)