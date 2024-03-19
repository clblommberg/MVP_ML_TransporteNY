## sesion 1
Máximo 5 integrantes y mínimo 4
Les vamos a ofrecer dos temas y uds van a elegir la que más les guste para desarrollar el PF
Por Slack verán un formulario de inscripción que deberán completar con nombre de integrantes y temática elegida .
Serán agregados a un canal de Slack de su grupo conjuntamente con su mentor. Organícense para comenzar las dailies con todo.


## Sprint #1
Comprensión de la situación actual: contextualizarla y expresar posibles análisis/ soluciones en torno a la misma.
Objetivos y alcance
Planteo de KPIs
Armar repo de Github para trabajar de manera colaborativa
Con qué herramientas van a realizar la arquitectura del proyecto
Estimación de la duración de cada tarea en diagrama de Gantt



- Seleción de Proyecto:
Propuesta 2: NYC 
- Integrantes:
Byron Torres
Claudio Valerio Quispe Alarcon
Duvan Eduardo Robayo Roa
Herlin Isaac Yauri Barrios

- Objetivos y alcance:
"Una empresa de servicios de transporte de pasajeros, que actualmente se encuentra operando en el sector de micros de media y larga distancia, está interesada en invertir en el sector de transporte de pasajeros con automóviles. Con una visión de un futuro menos contaminado y ajustarse a las tendencias de mercado actuales, quieren corroborar la relación entre estos medios de transporte particulares y la calidad del aire, como también la contaminación sonora, para estudiar la posibilidad de implementar vehículos eléctricos a su flota; ya sea en su totalidad o parte de la misma.

​Pero debido a que sería una unidad de negocio nueva, se pretende hacer un análisis preliminar del movimiento de los taxis en la ciudad de Nueva York, para poder obtener un marco de referencia y poder tomar decisiones bien fundamentadas.

​Tu equipo es contratado por dicha empresa, con el objetivo de acompañar al negocio, en ese proceso de toma de decisión, para lo cual deberán utilizar los datos provistos de mayor calidad encontrados, y cruzarlo con otros datos, como los ofrecidos por viajes compartidos, calidad del aire, contaminación sonora y correlaciones climáticas. Nota: Pueden agregar todos los datasets que consideren pertinentes para cumplir la propuesta de trabajo, pero es obligatorio cruzar el dataset de taxis con al menos otros dos (condición necesaria de aprobación). "


ahora con estos puntos necesito desarrollar estos puntos ?
Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos
En esta semana deben realizar un análisis del proyecto seleccionado y los datos disponibles. En base al entendimiento que logren de la temática, deben proponer como encararla, brindando una solución o herramientas desarrolladas por ellos mismos para acercarse a dicha solución.


Esta propuesta deberá contemplar los siguientes ítems:


Entendimiento de la situación actual
En la propuesta debe quedar manifiesto un adecuado manejo de la problemática, deben poder contextualizarla y expresar posibles análisis/ soluciones en torno a la misma.

Objetivos
Los objetivos deben ser acciones concretas (verbos) que describan claramente lo que buscan lograr con el proyecto. Desarrollar, crear, hacer, etc.


Alcance
Las temáticas suelen ser amplias y pueden admitir tratamientos mucho más abarcativos en extensión y magnitud de lo que puede realizarse durante el desarrollo del proyecto.

Es por esto que deberán delimitar su trabajo definiendo el alcance y las tareas/desarrollos que puedan considerar importantes para la integridad del proyecto pero que por complejidad o tiempo, estén fuera de alcance.

Esto último pueden plantearlo como posibilidades de continuidad del proyecto.


Objetivos y KPIs asociados (planteo)
Del entendimiento de la problemática surgirán cuestiones que se buscarán resolver con el trabajo o las herramientas desarrolladas. Estas cuestiones, formuladas como objetivos, admitirán la creación de KPIs para evaluar su cumplimiento. Es una tarea muy abarcativa y a la vez muy específica en torno tanto a la problemática como al enfoque elegido.


Por ejemplo: 

Temática: generación de CO2.
Un enfoque puede ser medir el impacto de la agricultura y el consumo de carne animal en la generación de CO2. Un objetivo puede ser reducir la producción de carnes animales en un 8% para 2027 y ese mismo objetivo evaluarse mediante un KPI.

Entonces, la medición del mismo va a poder permitir tomar decisiones de negocio basadas en datos.

Temática: aviones.
Comparar el retraso de todos los vuelos de la aerolínea de un semestre con respecto a otros. Además, compararlo con el promedio de la industria. Si se encuentra por encima, proponer una reducción de, por ejemplo, 2% para el semestre que viene, e ir aumentando ese porcentaje de reducción en un 1% por los próximos 5 años.


Repositorio Github
Armar un repositorio de Github para trabajar colaborativamente con todo el grupo. Debe ser público para que lo pueda ver tanto el mentor como el Product Owner. Van a tener que llevar adelante diferentes branches y controles de versiones de su propio trabajo.


Solución propuesta
Deben detallar qué tareas harán para cumplir los objetivos de trabajo propuestos previamente y cómo lo harán (metodologías de trabajo, forma de organización, distribución de tareas, roles de cada uno dentro del equipo, etc). También, deben detallar qué productos surgirán de su trabajo y en qué etapa los presentarán, teniendo en cuenta los requerimientos generales (entregables esperados) para cada etapa del proyecto.


A su vez, deben realizar una estimación de tiempo para cada tarea, contemplando los tiempos de ejecución globales y los hitos previstos para cada semana; y plasmar esa estimación en un diagrama de Gantt.


Una parte muy importante de la solución propuesta, es con qué herramientas (stack tecnológico) van a realizar la arquitectura del proyecto. Para esto, lo que van a tener que hacer es seleccionar una pequeña porción de los datos que disponen y realizar un proceso de limpieza y transformación utilizando las herramientas que planean implementar. Esto les dará una idea de cómo funcionarán en el proyecto completo y les permitirá tener un mejor abordaje para futuras tareas. Hay que tener en cuenta que, como este ítem va a ser una presentación previa de lo que van a trabajar en el segundo sprint, el PO puede dar el OK o determinar cuál es el mejor camino para que tomen. Esto les va a permitir adelantar trabajo de la segunda semana, ya que no se va a tener que esperar hasta la segunda demo para verificar si la arquitectura cumple con los requisitos del PO.


Finalmente, como en Data es muy importante trabajar con datos de calidad, deberán incluir en su informe un análisis sobre los datos con los que van a trabajar (metadatos), detallandolos lo más posible: fuentes y confiabilidad de las mismas, qué representa cada columna de cada dataset, tipos de datos, método de adquisición, fecha de adquisición y ultima actualización, etc.

Hitos
3 KPI’s
Documentar alcance del proyecto
EDA de los datos
Repositorio en Github
Implementación stack tecnológico
Metodología de trabajo
Diseño detallado
Equipo de trabajo - Roles y responsabilidades
Cronograma general - Gantt
Análisis preliminar de calidad de datos


Sprint #2
ETL completo
Estructura de datos implementada (DW, DL, etc). Pueden usar algún servicio
Pipeline ETL automatizado
Diseño del Modelo ER
Pipelines para alimentar el DW
Data Warehouse
Automatización
Validación de datos
Documentación
Diagrama ER detallado (tablas, PK, FK y tipo de dato)
Diccionario de datos
Workflow detallando tecnologías
Análisis de datos de muestra
MVP/ Proof of Concept de producto de ML ó MVP/ Proof of Concept de Dashboard


Sprint #3
Qué esperamos de este Sprint: 
Diseño de Reportes/Dashboards
KPIs
Modelos de ML
Modelo de ML en producción
Documentación
Selección del modelo, feature engineering
Informe de análisis
Video del proyecto realizado, para que, en caso de ganar, pueda ser presentado en la graduación final.

Para desarrollar un modelo con estas tablas, primero necesitamos identificar cómo se relacionan entre sí. Aquí hay un resumen de los campos que parecen relacionarse en las diferentes tablas:
---
1. **Tabla 1 (Taxi Data):**
   - `VendorID`: Identificador del proveedor de servicios.
   - `tpep_pickup_datetime` y `tpep_dropoff_datetime`: Fecha y hora de recogida y entrega del pasajero.
   - `passenger_count`: Número de pasajeros.
   - `trip_distance`: Distancia del viaje.
   - `PULocationID` y `DOLocationID`: Identificadores de ubicación de recogida y entrega.
   - `fare_amount`, `tip_amount`, `total_amount`: Información financiera sobre el viaje.
   - `payment_type`: Método de pago.
   - `trip_type`: Tipo de viaje.

2. **Tabla 2 (Green Taxi Data):**
   - `VendorID`: Identificador del proveedor de servicios.
   - `lpep_pickup_datetime` y `lpep_dropoff_datetime`: Fecha y hora de recogida y entrega del pasajero.
   - `passenger_count`: Número de pasajeros.
   - `trip_distance`: Distancia del viaje.
   - `PULocationID` y `DOLocationID`: Identificadores de ubicación de recogida y entrega.
   - `fare_amount`, `tip_amount`, `total_amount`: Información financiera sobre el viaje.
   - `payment_type`: Método de pago.
   - `trip_type`: Tipo de viaje.

3. **Tabla 3 (Dispatch Data):**
   - `dispatching_base_num`: Número de base de despacho.
   - `pickup_datetime` y `dropOff_datetime`: Fecha y hora de recogida y entrega del pasajero.
   - `PUlocationID` y `DOlocationID`: Identificadores de ubicación de recogida y entrega.
   - `SR_Flag`: Bandera de solicitud de servicio.
   - `Affiliated_base_number`: Número de base afiliada.

4. **Tabla 4 (High Volume For-Hire Services Data):**
   - `hvfhs_license_num`: Número de licencia de servicio de alto volumen.
   - `dispatching_base_num`: Número de base de despacho.
   - `request_datetime`: Fecha y hora de solicitud del servicio.
   - `pickup_datetime` y `dropoff_datetime`: Fecha y hora de recogida y entrega del pasajero.
   - `PULocationID` y `DOLocationID`: Identificadores de ubicación de recogida y entrega.
   - `trip_miles`: Millas del viaje.
   - `base_passenger_fare`, `tips`, `driver_pay`: Información financiera sobre el viaje.
   - `shared_request_flag`, `shared_match_flag`: Indicadores de solicitud y coincidencia compartidos.
   - `access_a_ride_flag`, `wav_request_flag`, `wav_match_flag`: Indicadores de diferentes tipos de solicitudes.

Para desarrollar un modelo, podríamos considerar fusionar estas tablas en función de los campos comunes, como los identificadores de ubicación, las fechas y horas de recogida y entrega, así como los identificadores de proveedor de servicios. Esto nos permitirá construir características más ricas y detalladas para predecir, por ejemplo, el costo del viaje, el tiempo de viaje o el método de pago. Dependiendo de la naturaleza específica del problema que estés tratando de abordar con el modelo, podrías necesitar un preprocesamiento adicional, como la limpieza de datos, la codificación de variables categóricas y la ingeniería de características.
---
### Marco Teórico:

1. **Taxi Data (Tabla 1):**
   - Esta tabla contiene datos sobre los viajes de taxis amarillos en la ciudad, incluyendo información como la fecha y hora del viaje, la duración, la ubicación de inicio y fin, la tarifa, etc. Cada registro en esta tabla representa un viaje en un taxi amarillo.

2. **Green Taxi Data (Tabla 2):**
   - Similar a la Tabla 1, pero contiene datos sobre los viajes de taxis verdes en la ciudad. Los taxis verdes suelen ser vehículos híbridos o eléctricos y pueden operar en áreas específicas de la ciudad.

3. **Dispatch Data (Tabla 3):**
   - Esta tabla proporciona información sobre la asignación de viajes a diferentes bases de despacho. Incluye datos como el número de base de despacho, la fecha y hora del viaje, la duración del viaje, etc.

4. **High Volume For-Hire Services Data (Tabla 4):**
   - Esta tabla contiene datos sobre los servicios de alquiler de alto volumen, que podrían incluir servicios de transporte compartido, servicios de viajes en grupo, etc. Incluye información como la fecha y hora del viaje, la duración, la ubicación de inicio y fin, etc.

### Estrategia de Relación:

Para relacionar la Tabla 3 (Dispatch Data) con la Tabla 4 (High Volume For-Hire Services Data), y luego con las Tablas 1 y 2, podríamos seguir este enfoque:

1. **Relación entre Tabla 3 y Tabla 4:**
   - Ambas tablas tienen datos sobre los viajes, por lo que podríamos relacionarlas mediante un campo común como la fecha y hora del viaje o algún identificador único del viaje.

2. **Relación entre Tabla 4 y Tabla 1 (Taxi Data):**
   - Podríamos relacionar estas tablas mediante la ubicación de inicio y fin del viaje, así como la fecha y hora del viaje. Los viajes en taxis amarillos (Tabla 1) podrían estar presentes en la Tabla 4 si son considerados servicios de alquiler de alto volumen.

3. **Relación entre Tabla 4 y Tabla 2 (Green Taxi Data):**
   - Similar a la relación con la Tabla 1, podríamos relacionar estas tablas utilizando la ubicación de inicio y fin del viaje, así como la fecha y hora del viaje. Los viajes en taxis verdes (Tabla 2) podrían estar presentes en la Tabla 4 si también son considerados servicios de alquiler de alto volumen.

En resumen, la estrategia de relación implica buscar campos comunes entre las diferentes tablas, como la fecha y hora del viaje, la ubicación de inicio y fin, o algún identificador único del viaje, para establecer relaciones entre ellas.
---

