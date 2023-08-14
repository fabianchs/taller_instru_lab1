# Introducción al taller de instrumentación

El presente laboratorio pretende introducir al estudiante al modelado y calibración de
señales dinámicas mediante lo siguientes objetivos específicos

- Elaborar un modelo matemático de un canal de comunicación.
- Practicar el uso de herramientas de análisis computacionales.
- Uso de herramientas de control de versiones.

## 1. Metodología
La metodología para el siguiente laboratorio permite definir los pasos necesarios para alcanzar los resultados propuestos.

### 1.1 Diseño del experimento


- La obtención de un modelo de respuesta en frecuencia de un dispositivo bajo prueba. Se utilizará un micrófono de audio y se repetirá tanto con el micrófono de un celular como el de una laptop.

- Se utilizará el modelo de estimación de respuesta en frecuencia por barrido de frecuencia de una señal sinusoidal. La emisión del audio será con un parlante, este reproducirá un audio que hace un barrido de frecuencia desde 50Hz hasta 5kHz.

- Con las grabaciones se hará el análisis de la respuesta en frecuencia de cada micrófono, ambos audios serán almacenados en formatos sin distorsión por compresión.

- Finalmente se elaborará un método para estimar el SNR de las grabaciones con 1kHz de tono como referencia.

### 1.2 Adquisición de datos
- La adquisición de datos será mediante los micrófonos de la laptop y celular, se asegurará una distancia de 1 a 2 metros entre el parlante y el celular/laptop. Cada audio se almacenará y enviará para su análisis.

### 1.3 Procesamiento de datos
- Esta parte implica la sincronización del barrido fuente con el barrido experimental, con el fin de comparar exactamente cada punto en frecuencia del audio y así obtener la función de transferencia del audio obtenido. No se modificará la ecualización ni volumen del audio.
  
### 1.4 Analisis y obtención de función de transferencia
- Mediante algún lenguaje de programación se obtendrá un análisis de ganancia de los datos adquiridos a través del tiempo, de esta forma se obtiene la función de transferencia de la comparación entre la referencia y el audio grabado, con esta información es posible generar un gráfico de respuesta en frecuencia, este permitirá visualmente notar si el micrófono tiene algun filtro en su circuito de procesamiento, mediante atenuaciones o ganancias significativas.
  
### 1.5 Comparación de datos
- Se realizarán comparaciones a partir del audio de referencia con el grabado según el tipo de micrófono, de esta forma se discutirán las diferencias más significativas entre cada función de transferencia, del mismo modo será posible notar el rango de obtención de audio de cada micrófono y los filtros que tengan.
  
### 1.6 Justificación y conclusión de resultados
- Se describirán las herramientas matemáticas y de programación utilizadas para alcanzar los objetivos propuestos y la explicación que permitió obtener la solución para cada función de transferencia. Del mismo modo se expondrán los objetivos alcanzados y los pasos necesarios que permitieron la realización del laboratorio.

## 2. Cuestionario previo

### 2.1 ¿Cómo se mide el signal-to-noise ratio (SNR) para una señalanalógica? Brinde un ejemplo
Es la proporción existente entre la potencia de salida de la señal que se transmite y la potencia del ruido que interfiere con ella, además, se mide en decibeles [0].

Una forma de medirlo es usando un analizador espectral de la señal con la cual se pueda apreciar la forma de la señal y el ruido en el dominio de la frecuencia, se hace una integral de ambas señales y luego se usa la expresión del SNR para obtener el valor final [1]. A continuacion se muestra la expresion para el calculo del signal-to-noise (SNR).

$$SNR = 10\log_{10} \left( \frac{P_{s}}{P_{n}} \right)$$



### 2.2 ¿Cuál es el ancho de banda típico para señales de audio? ¿Una señal de audio tiene componente DC?

De 20Hz a 20Khz ya que según la capacidad auditiva humana solo es posible escuchar sonidos que se encuentran en el rango de frecuencia mencionado anteriormente [2]. 

Toda señal de audio que no haya sido debidamente limpiada de interferencias de bajas o altas frecuencias, tanto en grabación, mezcla o mastering por medio de filtros, son posibles portadoras de desplazamiento de DC [3]. 

### 2.3 ¿Cómo afecta el ruido térmico al SNR de una señal analógica? ¿Cuántos dBm tiene el ruido térmico para una impedancia de 50Ω para una señal cuyo BW= 20kHz?
Es un ruido aleatorio que se genera por la agitación térmica de los portadores. Su espectro de frecuencias es plano, es un ruido blanco. Se genera en cualquier elemento que se comporte como una resistencia.

Eso significa que mientras mas alta sea la temperatura, los portadores de carga tendrán una mayor energía (mas ruido), por lo tanto, al captar un sonido mediante un micrófono que se comporta como una resistencia, este aunque su temperatura no sea alta, de igual forma posee portadores de electrones que producen ruido [4].

El ruido termico para una impedancia de 50Ω para una señal a 20kHz a temperatura ambiente es de -89.05dBm [5].

### 2.4 ¿Qué es ruido de cuantización? ¿Bajo qué circunstancias se podría modelar como ruido activo?
El error de cuantización es la técnica de representar una señal analógica con un número digital, en general es la conversión analógica a digital de una señal en específico [9].

### 2.5 ¿Para una grabación de audio, el piso de ruido de la señal es predominado por el ruido de cuantización o el ruido térmico?
Es determinado por el ruido térmico. El ruido térmico o de Johnson es el ruido resultante del movimiento aleatorio de los electrones debido a su agitación térmica. El movimiento da a lugar una corriente aleatoria en consecuencia aparece una tensión de ruido V_r [7].

### 2.6 ¿Cuáles son las tasas de muestreo más populares para grabaciones de auido? ¿La cantidad de bits por muestra?

La frecuencia de muestreo es la cantidad de muestras que se toman por unidad de tiempo para convertir una señal analógica en digital. A nivel general las frecuencias de muestreo utilizadas en los medios digitales han sido 44.1kHz y 48kHz. 
Por la parte de los bits, esta define el rango dinámico del sonido, cuanto mayor es la tasa de bits, se dispone de mayores posicione para ubicar la muestra tomada en la onda. El estándar general es de 44.1kHz a 16bits, para grabaciones de mayor calidad se utiliza una de 32bits. [8]


### 2.7 ¿Cuales son los formatos de audio cuya compresión o almacenamiento no agrega distorsión?

Algunos de los formatos de audio sin pérdida más conocidos son:FLAC (Free Lossless Audio Codec), ALAC (Apple Lossless Audio Codec), WAV (Waveform Audio File Format), APE (Monkey's Audio)[6].

### 2.8 ¿Cómo se puede utilizar un barrido de frecuencias para modelar la respuesta en frecuencia de un dispositivo bajo prueba (DUT)? Investigue el procedimiento a realizar a cada grabación de audio para tener la estimación de la respuesta en frecuencia

Se creará una señal de prueba que contenga un barrido de frecuencia de 50 a 5kHz. Ahora con la utilización de un software de análisis de señales se captura y graba el audio recibido por el dispositivo de prueba. Utilizaremos un analizador de espectro para obtener la respuesta en frecuencia del audio grabado. Por último, se normalizan los datos y se promedian múltiples mediciones para obtener una mayor precisión[2].

## 3. Resultados

Para la obtención de resultados se utilizó un celular y una tablet, posteriormente se utilizó el entorno de matlab para obtener la transformada de Fourier para cada audio, de esta manera se graficó cada grabación y se obtuvo la respuesta en frecuencia respectivamente.

La formulación para la transformada de Fourier es la siguiente:

![Alt text](images/fourier_tr.png)

### 3.1 Transformada de Fourier del audio original
<br>

![Alt text](images/plot_audio_original.jpg)

### 3.1 Transformada de Fourier del audio grabado con celular

<br>


![Alt text](images/plot_audio_phone.jpg)


### 3.1 Transformada de Fourier del audio grabado con laptop


<br>

![Alt text](images/plot_audio_pc.jpg)
## 4. Referencias
[0] R. Alonso. "Relación señal-ruido o SNR en audio: ¿qué es y por qué importa?" HardZone. https://hardzone.es/reportajes/que-es/relacion-senal-ruido-snr-audio/ (accedido el 6 de agosto de 2023). 

[1] Universitat Politècnica de València - UPV. (2022, 4 de abril). Cálculo de la relación señal a interferencia más ruido (SINR) | | UPV [Video]. YouTube. https://www.youtube.com/watch?v=oLeWP9fIoZ8

[2] R. Sousa. "La señal de audio, conceptos y medidas – TM Broadcast". TM Broadcast – Ingeniería y Tecnología broadcast audiovisual. https://tmbroadcast.es/index.php/la-senal-de-audio-conceptos-y-medidas/ (accedido el 6 de agosto de 2023). 

[3] "DC Offset, Lo Que Siempre Quisiste Saber Y Nadie Te Supo Explicar - Sound:check Magazine". Soundcheck Magazine. https://soundcheck.com.mx/dc-offset-lo-que-siempre-quisiste-saber-y-nadie-te-supo-explicar/ (accedido el 6 de agosto de 2023). 

[4] "RUIDO EN AMPLIFICADORES - PCPfiles en www.pcpaudio.com". PCP audio. https://www.pcpaudio.com/pcpfiles/doc_amplificadores/Bajoruido/Bajoruido.php (accedido el 6 de agosto de 2023). 

[5] M. J. M. Pelgrom, "Analog-to-digital-conversion," 2nd ed. Springer, 2013.

[6] Formatos de audio: Todo lo que Los Músicos deberían Saber para Elegir El Archivo Adecuado (2023b) LANDR Blog. Disponible en: https://blog.landr.com/es/guia-formatos-de-audio/ (Accedido: 06 August 2023). 

[7] UIB. “Ruido”. [En línea]. Disponible en http://dfs.uib.es/GTE/education/telematica/sis_ele_comunicacio/Apuntes/Capitulo%203.pdf


[8] Multisononline J. "Frecuencia de muestreo: Qué es y cómo calcularla".  [En línea]. Disponible en: https://multisononline.com/blog/de-analogico-a-digital-frecuencia-de-muestreo-y-tasa-de-bits-n267. Acceso: 6 de agosto de 2023.

[9] M. J. M. Pelgrom, Analog-to-Digital Conversion, 2nd ed. Dordrecht, Netherlands: Springer Science+Business Media, 2013.
