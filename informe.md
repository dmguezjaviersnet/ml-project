# Informe Proyecto Machine Learning 2022.

## Integrantes

- Javier E. Domínguez Hernández C-412
- David Orlando De Quesada Oliva C-411
- Andrés Alejandro León Almaguer C-412


### El problema

Nuestro proyecto se enfoca en el problema de tratar de predecir cuando un vehículo en 
su trayecto por la vía, se encuentra con una anomalía (bache, juntas de expansión, líneas de tren, banda de frenado, etc). 

### La propuesta y los datos
	
Nuestra propuesta es utilizar los sensores de los teléfonos móviles como el acelerómetro, el giroscopio y el GPS
para construir un modelo de Machine Learning que sea capaz de predecir la ocurrencia de estos eventos mientras el 
vehículo está en movimiento. Inicialmente nuestra idea es analizar los datos del acelerómetro en los tres ejes del
dispositivo, el X (que va de un lado a otro del dispositivo), Y (que va de la parte de abajo hacia la parte de arriba del móvil) y
Z (que atraviesa la pantalla del móvil de un lado a otro). Con la hipótesis de que una verdadera anomalía en un intervalo de tiempo
produce un pico en la señal del acelerómetro (serie temporal) en el eje Z, pues el vehículo cae por un periodo breve de tiempo. Creemos que esta es la 
característica principal de una anomalía, pero no creemos que sea suficiente para diferenciar por ejemplo, un bache en un solo lado del vehículo
de una línea de tren. Hay otros features que consideramos pueden ayudar mejorar la precisión del modelo:

- La lectura del acelerómetro en el eje X. Esta lectura creemos que puede ayudarnos a mejorar la precisión, pues un bache de un solo lado del 
vehículo también producirá un pico en dicha lectura, producto de que el carro se inclinará súbitamente hacia un lado.

- El cociente entre las lecturas del acelerómetro en los ejes X y Z (X/Z) es una característica extra que pensamos pueda impactar positivamente
en la clasificación de una anomalía. Esta característica sobre todo permite discernir entre anomalías que afectan al vehículo de igual forma a ambos lados,
o sea, anomalías que están a lo largo de la carretera, como líneas de tren, juntas de expansión o bandas de frenado.

- La velocidad también es un feature importante, pues a grandes velocidades, incluso pequeñas anomalías pueden mostrar picos considerables en las 
lecturas del acelerómetro (y posiblemente del giroscopio). A muy baja velocidad las anomalías se sienten mucho menos pues los cambios son menos súbitos
en las lecturas. Del feature anterior se deriva otro que consideramos importante, el cociente Velocidad/acelerómetro-Z.

- Las lecturas del giroscopio también creemos que son features que puede ayudarnos a mejorar la calidad de la predicción, pues el móvil puede girar
alrededor de algún eje específico o varios, que sea característico de alguna anomalía en particular. Aún debemos recolectar datos para analizarlos
y poder tomar una decisión definitiva. Es importante destacar que el sensor que proporciona estos datos no está disponible en muchos móviles de gama baja
principalmente, por lo que no le daremos tanta prioridad a la hora de incorporarlo al modelo.

- El GPS planeamos utilizarlo para etiquetar algunas anomalías, para de esta forma, cuando un vehículo registre una anomalía en coordenadas
semejantes a donde se etiquetó esa anomalía, poder clasificar una anomalía en un tipo u otro.

Nuestra idea para entrenar nuestro modelo es utilizar algún algoritmo de clustering, K-means o preferiblemente DBSCAN para detectar las anomalías que no son
más que outliers en nuestro dataset. Luego pretendemos utilizar los datos etiquetados a mano, para poder asignar etiquetas a cada cluster y poder saber que
tipo de anomalía es la que se encuentra en cada cluster, de esta forma estaríamos construyendo un modelo de aprendizaje semi-supervisado 

### Resultados
	
La velocidad la estamos calculando utilizando el GPS, debido a la latencia entre una lectura y otra de este sensor, la velocidad tiene picos anormales 
que debemos tratar de corregir, o computar la velocidad de otra forma.


