# PROYECTO FINAL DATA SCIENCE
**---**
FOTO DATADIIP Y TAXIS
## INTRODUCCIÓN Y CONTEXTO
>La ciudad de Nueva York ha tenido un crecimiento acelerado en las últimas décadas, la que cuenta con más de 8 millones de habitantes en su zona urbana y más de **22 millones de habitantes en la zona metropolitana**. A su vez, cuenta con una densidad de **10.756 habitantes por kilometro cuadrado** según fuentes oficiales. Debido a esto, los desafíos que enfrenta en términos de transporte son importantes. En promedio una persona gasta más de **40 minutos para llegar a su trabajo** y su sistema de transporte cuenta con opciones como el metro, autobuses, bicicleta y taxis que están regulados por la **Comisión de Taxis y Limosinas (TLC)** y el **Departamento de Transporte de la Ciudad de Nueva York (DOT)**.

Una empresa de servicios de transporte de pasajeros, que actualmente se encuentra operando en el sector de micros de media y larga distancia, **está interesada en invertir en el sector de transporte de pasajeros con automóviles en Nueva York**. Con una visión de un futuro menos contaminado y ajustarse a las tendencias de mercado actuales, quieren, además de investigar la rentabilidad del negocio, verificar la relación entre este tipo de transporte y la calidad del aire, así como otras externalidades. Esto, con la finalidad de estudiar la posibilidad de implementar vehículos eléctricos a su flota; ya sea en su totalidad o parte de la misma.

​Debido a que se trataría de una unidad de negocio nueva, **se pretende hacer un análisis preliminar del movimiento de los taxis en la ciudad de Nueva York**, para tener un marco de referencia y poder tomar decisiones justificadas.

## PROPUESTA DE TRABAJO
Recopilar, depurar y disponibilizar la información: **Creación de una base de datos (DataWarehouse)** con información proveniente de diferentes fuentes, corriendo en local o alojada en proveedores en la nube. La base de datos depurada **deberá contemplar por lo menos dos tipos diferentes de extracción de datos**, como datos estáticos, llamadas a una API, scrapping, entre otros. 
El análisis **debe contemplar las relaciones entre variables** y concluir, si es que hubiera, una relación entre estas, y los posibles factores que pueden ocasionar dicha relación.
Por último, **se deberá generar un modelo de machine learning** de clasificación supervisado o no supervisado, entrenado y puesto en producción: Este modelo deberá resolver un problema y conectar globalmente con los objetivos propuestos.

## PROCEDIMIENTO

#### 1. EXTRACCIÓN
Se identificaron fuentes de datos relevantes para el estudio y se obtuvieron ya sea de forma manual o mediante webscrapping (extracción de forma automatizada), una cantidad relevante de datasets para su posterior análisis.

#### 2. ANÁLISIS EXPLORATORIO DE DATOS (EDA), TRANSFORMACIÓN Y LIMPIEZA
En este punto, se procedió a limpiar y preprocesar los datos extraídos para eliminar aquellos que tienden a estar fuera de rango (outliers), registros que están duplicados, datos incorrectos y/o faltantes, y así formatearlos según sea necesario.

#### 3. CARGA
Al trabajar con grandes volúmenes de registros, es necesario cargar y almacenar los datos generados en la nube, mediante una herramienta de Datawarehouse o Datalake, ya que estos otorgan características importantes para el trabajo con datos, como lo son almacenamiento, seguridad y organización (muy importante en el primer caso).

#### 4. ANÁLISIS DE DATOS Y MODELO DE MACHINE LEARNING
Una vez realizados los pasos anteriores, se procedió de manera paralela a analizar y visualizar los datos obtenidos y a generar un modelo de Machine Learning (ML) que responda a los objetivos planteados. Para el primer caso, se exploraron e identificaron tendencias y se monitorearon métricas clave o indicadores de rendimiento (KPIs) para poder tomar decisiones informadas respecto al propósito del proyecto. A su vez, la creación del modelo de ML tuvo como objetivo generar predicciones de demanda de vehículos en los diferentes sectores de Nueva York. 
#### 5. DEPLOY EN LA WEB DE LOS RESULTADOS OBTENIDOS
Se creó una página web donde se presentan los principales resultados de este estudio. 