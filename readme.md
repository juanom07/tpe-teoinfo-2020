# Teoría de la Información 2020

## Trabajo Especial

<div align="justify">
Durante los años ‘80, cosas extrañas ocurrieron en la ciudad de Hawkins cuando un niño llamado Will Byers desapareció en un universo paralelo.
Su madre Joyce acudió a la estación de policía con una fotografía de su hijo para realizar la denuncia, y obtener algún dato sobre el paradero del niño.
El oficial de guardia tomó la foto que llevó Joyce y la ingresó en el Sistema Informatizado de Datos de Personas Encontradas (SIDPE) para cotejar con fotos de otros muchachos encontrados recientemente en las ciudades cercanas a Hawkins.
Tras un largo procesamiento, el sistema arrojó 5 (cinco) fotos de niños parecidos a Will.
</div>

<div align="right">
<img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will(Original).bmp" width="131" height="170"></div>
Resolver:

* Dada la foto Will(Original).bmp que llevó Joyce a la estación de policía y la lista de fotos obtenidas por el sistema de búsqueda, implementar un algoritmo que permita ordenar la lista según su parecido con la foto de Will que entregó Joyce, utilizando el factor de correlación como medida de similitud. Analizar los resultados obtenidos.
	<div align="center">
	<img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_1.bmp" width="131" height="170">    <img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_2.bmp" width="131" height="170">    <img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_3.bmp" width="131" height="170">    <img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_4.bmp" width="131" height="170">    <img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_5.bmp" width="131" height="170">
	</div>

* Un policía amigo de Joyce llegó a la estación de policía un rato más tarde, trayendo consigo otra foto para analizarla. El policía de guardia, para ahorrarse la búsqueda en el SIDPE, propuso estudiar las similitudes respecto a la imagen que llevó Joyce mediante esta estrategia a implementar: Obtener la distribución de intensidades de la imagen de la foto que llevó Joyce, de la foto del niño más parecido (obtenida por el sistema de búsqueda) y de la foto que tenía el policía en su billetera. Generar el histograma de cada imagen y calcular la media y el desvío de cada distribución. Analizar las similitudes y diferencias entre uno y otro indicador.

* Implementar un algoritmo que permita codificar una imagen mediante el método de Huffman y posteriormente reconstruirla mediante otro algoritmo decodificador (el archivo comprimido deberá contener la secuencia de bits codificados junto con los datos necesarios para la reconstrucción de la imagen original). Con dicho algoritmo codificador:
    1. Comprimir con Huffman semi-estático la imagen original.
    1. Comprimir la imagen del resultado más parecido con el código de Huffman asociado a la imagen original.
    1. Comprimir la imagen que trajo el policía con el código de Huffman asociado a la imagen original.
    1. Comprimir la imagen que trajo el policía utilizando Huffman semi-estático, esta vez utilizando el código generado para la propia imagen. Comparar con el resultado del inciso anterior.
    1. Comparar las tasas de compresión obtenidas por las compresiones en los ejercicios (a), (b), (c) y (d).
  **Nota**: el algoritmo decodificador deberá permitir reconstruir los datos generados por el codificador y obtener la imagen original.
* Tres canales de televisión distintos (Canal 2, Canal 8 y Canal 10) transmiten todos los días la fotografía de Will. Sin embargo, un fenómeno extraño hace que cada canal distorsione las imágenes de diferente forma. Al notarlo, el comisario de policía decidió estudiar el ruido de cada uno, esperando que esta información permita encontrar al joven Will. Considerando que la imagen de entrada a cada canal es la foto de Will provista por su madre al llegar a la estación de policía, y las imágenes a la salida de cada canal son las siguientes, resuelva:
    1. Implementar un algoritmo que calcule la matriz de transición que describe cada canal.
    1. Implementar un algoritmo que calcule el ruido de cada canal utilizando muestreo computacional. Generar un gráfico que permita estudiar la evolución del error y la convergencia.

<div align="center">
<img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_Canal2.bmp" width="131" height="170">
Canal 2
<img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_Canal8.bmp" width="131" height="170">
Canal 8
<img src="https://github.com/juanom07/tpe-teoinfo-2020/blob/master/ImagenesWill/Will_Canal10.bmp" width="131" height="170">
Canal 10
</div>

  **Nota**: Todas las imágenes necesarias para resolver el trabajo especial son del mismo tamaño y tienen las mismas intensidades de gris, y se encuentran disponibles en la sección “Trabajo Especial” de la página web de la cátedra.

## Pautas para la entrega del Trabajo Especial

Un informe en PDF (no más de 10 páginas sin contar la portada) que incluya los siguientes ítems: 
Título del trabajo, identificación de los integrantes y e-mail de contacto. 
Resumen: de qué se trata el trabajo y qué se estudia. 
Introducción: breve descripción del problema tratado.
Desarrollo: explicación de los cálculos realizados y planteo de pseudocódigos de los algoritmos utilizados, análisis de los resultados, comparaciones, gráficos, etc.
**NOTA**: utilizar pseudocódigos para describir en el informe los algoritmos implementados (no código fuente).
Conclusiones: qué se hizo en el trabajo y qué resultados se obtuvieron.

## Tener en cuenta

Todos los resultados deberán ser adecuadamente interpretados y/o justificados de acuerdo al problema. 
Los algoritmos desarrollados deben ser claramente explicados y se debe plantear el pseudocódigo correspondiente en el informe. 
No incluir código fuente ni cálculos o tablas auxiliares dentro del cuerpo del informe (si se considera relevante, puede incluirse en un apéndice)
