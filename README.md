![Sobre](public/v1.jpg)
---
`En este archivo encuentra la introducción sobre la situación de la movilidad en transporte en Nueva York`
---
![Intro](public/v3.jpg)

>La ciudad de Nueva York ha tenido un crecimiento acelerado en las últimas décadas, la ciudad cuenta con más de 8 millones de habitantes en su zona urbana y más de **22 millones de habitantes en la zona metropolitana**, cuenta con una densidad de **10.756 habitantes por kilometro cuadrado** según fuentes oficiales. Los desafíos en transporte también son relevantes, en promedio una persona gasta más de **40 minutos para llegar a su trabajo** y el sistema de transporte está compuesto de opciones como el metro, los autobuses, la bicicleta y los taxis regulados por la **Comisión de Taxis y Limosinas (TLC)** y el **Departamento de Transporte de la Ciudad de Nueva York (DOT)**.

Según el **Plan Estratégico de la ciudad** existen 6 oportunidades de mejora en materia de transporte para mejorar la calidad de vida de los neoyorquinos en los que se destaca: mejorar la seguridad vial en las calles con la implementación del programa **publición Cero**, expandir la **red de ciclorutas**, mejorar el tránsito para el **transporte público**, mejorar el **transporte de carga** debido a que la ciudad tuvo una explosión de compras en línea y entregas puerta a puerta, implementar un **sistema de aparcamiento inteligente** y un sistema de movilidad centrado en la **sostenibilidad**. Para ver más acerca de este reporte puede consultar la [Documentación](https://github.com/clblommberg/MVP_ML_TransporteNY/blob/main/datasets/docs/Strategic-plan-2016.pdf)
>
> ![Alcance](public/v4.jpg)
>
> ## ¿Por qué metodología ágil y no tradicional?
> 
> > Esta elección se basa en la necesidad de **adaptabilidad**, **rapidez** y **comunicación** en un periodo de tiempo corto. Esta metodología nos permite:
> > 
> > ### Flexibilidad
> > 
> > > Responder rápidamente a los ajustes, solicitudes y retroalimentaciones del proyecto al establecer **fechas de entrega semanales** con el Product Owner.
> > 
> > ### Incrementalidad
> > 
> > > El producto se alimentará de varios **entregables semanales**, esto nos permite asegurar **productos mínimos viables** antes de finalizar cada semana que pueden ser evaluados por el Product Owner y ajustados antes del inicio del próximo sprint. 
> > 
> > ### Colaboración y comunicación de equipo
> > 
> > > Al trabajar en ciclos cortos y tener reuniones diarias, se mantiene a todo el **equipo informado** del progreso del proyecto, compartir ideas y resolver problemas de manera colaborativa.
> > 
> > ### Planeación semanal
> > 
> > > En este caso la planificación de las tareas se hace de manera **semanal**, un enfoque menos estricto y más realista en tiempo que el propuesto en las metodologías tradicionales, que permite asignar las tareas a las **necesidades** del proyecto semanal.
> 
> ![SCRUMBAN](public/v2.jpg)
>
> ## ¿Por qué SCRUMBAN?
> 
> > Este marco de trabajo es una combinación única de estructura y flexibilidad que nos permite aprovechar las ventajas de ambas metodologías con un un enfoque más **adaptable** y **menos estricto**.
> > 
> > ### Flexibilidad
> > 
> > > Ofrece la estructura y prepublicibilidad de **Scrum**, con sus iteraciones regulares y eventos definidos, junto con las prácticas flexibles, capacidad de respuesta y mejora continua de **Kanban**.
> > 
> > ### Adaptabilidad
> > 
> > > Nos permite **adaptar el proceso** a medida que evolucionan los sprints del proyecto, utilizar más prácticas de Scrum cuando se necesite mayor **planificación y estructura**, o Kanban, cuando se requiera mayor capacidad de **respuesta y flexibilidad**.
> > 
> > ### Gestión del flujo de trabajo
> > 
> > > El uso del tablero de Kanban permite **publicualizar y controlar** el progreso de las tareas, y los **límites de trabajo** en progreso (WIP) ayudan a evitar el exceso de trabajo y los cuellos de botella.
> > 
> > ### Colaboración y transparencia
> > 
> > > Los tableros de progreso son **publicibles para todos**, lo que facilita la comunicación y la colaboración en torno a las tareas y objetivos del proyecto.
---
![ciclo](public/v5.jpg)

> En cada uno de los sprints existen unas **actividades predefinidas** que establecen la organización del trabajo semanal, estas actividades son:
> 
> ## Definición de requerimientos
> 
> > Se republican las solicitudes del Product Owner en cuanto a las **necesidades del cliente**, se establecen los **objetivos de la semana** y qué **productos** se van a entregar al finalizar el sprint.
> 
> ## Creación y asignación del backlog
> 
> > Se crean las **tareas del equipo** y se hace una **planificación y asignación** de estas tareas teniendo en cuenta los requerimientos semanales.
> 
> ## Ejecución del sprint
> 
> > **Se desarrollan las tareas** del sprint por cada uno de los integrantes según la asignación del backlog,y se realiza **seguimiento** a través de reuniones diarias.
> > 
> 
> ## Presentación del sprint
> 
> > Se organiza previamente la **presentación** al Product Owner de los requerimientos de la semana y se establece un periodo de tiempo en el que se realizará la presentación. 
> 
> ## Ajustes del sprint
> 
> > De acuerdo a la retroalimentación dada por el Product Owner se **efectúan las correcciones** antes del inicio del siguiente sprint.
> > 

![roles](public/v6.jpg)

> La definición de roles nos permite **orientar las actividades** del grupo en función de las **habilidades y experiencias** previas del grupo, sin embargo la metodología escogida nos permite ejecutar estos roles de una manera **más fléxible**, en donde los roles se pueden intercambiar a medida de las **necesidades** del proyecto.
> 
> 
> ## Roles metodológicos
> 
> > Esta agrupación de roles nos permite **organizar la estructura del trabajo** y evitar posibles desviaciones en la ejecución de las tareas, se pueden considerar **roles organizacionales** dentro del equipo y su único fin es mejorar la **eficiencia y productividad** del equipo de trabajo.
> >
> > ### Sprint planner
> > > 
> > > Su rol está enfocado en establecer una planificación dinámica, su objetivo es llevar al equipo a la culminación de las tareas de la semana y proponer acciones para resolver posibles obstáculos.
> > > 
> > > - Republica junto al grupo los obstáculos y buscan resolverlos.
> > > - Crea las tareas que se realizarán en la semana en el tablero Kanban.
> > > - Pregunta por la asignación de las tareas.
> > 
> > ### Sprint moderator (Es dinámico, cada semana cambia)
> > > 
> > > Su rol está enfocado en dinamizar las reuniones diarias del grupo con el objetivo de **priorizar la ejecución de tareas** del grupo y evitar desviaciones de los objetivos de las reuniones.
> > > 
> > > - Republicar el orden del día acorde a la planificación de tareas.
> > > - Moderar las reuniones del equipo en función de los objetivos de la reunión.
> > > - Evita desviaciones de los objetivos de las reuniones.
> > > - Controlar los tiempos de las reuniones y el respeto por estos espacios.
> > 
> > ### Sprint team
> > 
> > > Todos los miembros del equipo hacen parte del Sprint Team y por lo tanto adquieren las mismas responsabilidad en el cumplimiento de las tareas planteadas.
> > >
> > > - Escogen sus tareas de acuerdo a sus habilidades y compromiso.
> > > - Participan y proponen ideas en las reuniones del equipo.
> > > - Reparten sus tareas adecuadamente y se preocupan por el proyecto.
>
> ## Roles Data Science
> > 
> > ### Data Architect
> > 
> > > Diseña y gestiona la arquitectura de los datos para garantizar que se capturen, almacenen, procesen y utilicen de manera eficiente y efectiva.
> > > - Establece el plan para la estructura de los datos asegurando coherencia con los objetivos del proyecto.
> > > - Desarrolla modelos y esquemas de los datos.
> > > - Diseña estrategias para integrar los datos de múltiples fuentes.
> > > - Define las políticas de gobierno de datos.
> > 
> > ### Data Analyst
> > 
> > > Extrae información significativa que pueda ayudar a la toma de decisiones y al logro de los objetivos organizacionales.
> > > - Usa técnicas y herramientas estadísticas para explorar los conjuntos de datos e identificar información.
> > > - Limpia y prepara los datos para su análisis.
> > > - Crea y presenta informes con el uso de herramientas de storytelling y publicualización.
> > > - Utiliza modelos de predicción para analizar resultados futuros.
> > 
> > ### Data Engineer
> > 
> > > Diseña, construye y mantiene los sistemas y arquitecturas que permiten el procesamiento y análisis eficiente de grandes volúmenes de datos.
> > > - Crea y mantiene flujos de trabajo robustos y escalables que reúnan datos de diferentes fuentes y realicen un proceso de ETL.
> > > - Integra datos de diferentes fuentes.
> > > - Diseña, implementa y gestiona almacenes de datos de forma eficiente.
> > > - Optimiza el rendimiento de los sistemas de datos mediante indexación y ajustes.
> > 
> > ### Machine Learning Engineer
> > 
> > > Diseña, implementa y mantiene los sistemas de aprendizaje automático para realizar modelos de predicción.
> > > - Establece los conjuntos de datos que usará para entrenar los modelos de aprendizaje y normalizar para un mayor rendimiento.
> > > - Diseña, implementa y evalúa modelos de aprendizaje automático.
> > > - Ajusta y optimiza los hiperparámetros para mejorar el rendimiento y precisión del modelo.
> > > - Implementa los modelos entrenados en APIs y servicios en la nube.

![eventos](public/v7.jpg)

> Se realiza una definición de las principales actividades que se van a desarrollar durante el desarrollo del proyecto y ayudarán a establecer la comunicación y la asignación de tareas.
> 
> ## Sprints
> 
> > El desarrollo del proyecto se dividirá en Sprints con una semana de duración, inician los días Lunes y finalizan el día viernes con la presentación de los entregables de esta semana.
> >
> > ### Sprint 1 - Planeación y acercamiento al proyecto
> > > 25 | Marzo | 2024 → 29 | Marzo | 2024
> > > Su objetivo es acercar al equipo de trabajo al proyecto planteado, establecer los alcances, la metodología y organización del proyecto.
> > > - **ENTREGABLE:** Documentación del stack tecnológico y el flujo de trabajo.
> >
> > ### Sprint 2 - Data Engineering
> > > 01 | Abril | 2024 → 05 | Abril | 2024
> > > Su objetivo es establecer el flujo de trabajo de los datos y establecerlos a un nivel de calidad que permita analizarlos.
> > > - **ENTREGABLE:** Documentación del ETL, pipeline, modelo ER y el MVP.
> >
> > ### Sprint 3 - Data Analytics & ML
> > > 08 | Abril | 2024 → 12 | Abril | 2024
> > > Su objetivo es crear las publicualizaciones que serán la herramienta de la presentación y el modelo de aprendizaje en función de los objetivos planteados.
> > > - **ENTREGABLE:** Documentación del dashboard y el modelo de Machine Learning.
> >
> > ### Sprint 4 - Data plus
> > > 15 | Abril | 2024 → 19 | Abril | 2024
> > > Su objetivo es detallar la documentación, realizar el video de presentación, establecer el Storytelling de la sustentación y trabajar en los adicionales.
> > > - **ENTREGABLE:** Documentación final, video y adicionales.
>
> ## Reuniones
>
> > Se presentan las diferentes reuniones que tendrá el equipo para comunicar sus avances, problemas y tomar decisiones sobre el proyecto.
> >
> > ### Sprint Planning
> > (60 minutos) 10:30 AM 🇦🇷 | 8:30 AM 🇨🇴
> >
> > > Se realiza todos los lunes y determina la ruta de trabajo de la semana.
> > > - Se republican las tareas en el tablero Kanban.
> > > - Se dividen las tareas en función de las habilidades del equipo.
> > > - Se republican los resultados de la retroalimentación (si la hay).
> >
> > ### Daily Scrum
> > (30 minutos) 10:30 AM 🇦🇷 | 8:30 AM 🇨🇴
> >
> > > Se realiza de martes a jueves y consiste en actualizar los avances realizados por el equipo.
> > > - Cada integrante muestra lo que realizó el día anterior y lo que realizará en el día.
> > > - Se informa si existen dificultades de avance.
> > > - Se determina como se solucionarán los obstáculos.
> > > - Se determina los avances que se mostrarán al mentor y las dudas.
> >
> > ### Sprint Review
> > (30 minutos) 02:00 PM 🇦🇷 | 12:00 MM 🇨🇴
> >
> > > Se realiza reunión con la mentora asignada al equipo de trabajo.
> > > - Se presentan las dudas y avances del proyecto.
> >
> > ### Sprint Demo
> > (30 minutos) 02:00 PM 🇦🇷 | 12:00 MM 🇨🇴
> >
> > > Se realiza reunión con el Product Owner los días viernes.
> > > - Se presentan los resultados del trabajo de la semana.
> > > - Se anotan los comentarios de la retroalimentación del product owner.
> >
> > ### Sprint Feedback
> > (15 minutos) 02:00 PM 🇦🇷 | 12:00 MM 🇨🇴
> >
> > > Se realiza reunión posterior al Sprint Demo.
> > > - Se republican los comentarios de la retroalimentación del product owner.
> > > - Se establecen tareas para corregir los aspectos de la retroalimentación antes de la reunión de inicio Sprint.
> >
> > ### Sprint Support
> >
> > > Reuniones de apoyo determinadas por el equipo para:
> > > - Resolver dudas.
> > > - Comunicar algún problema.
> > > - Capacitar a los miembros del equipo sobre algún tema.
>
![herramientas](public/v8.jpg)

> Se establecen las herramientas necesarias para la organización del trabajo, la colaboración y la comunicación.
> 
> ## Sprint Backlog
> 
> > Es una lista semanal de todas las tareas que el equipo se compromete a realizar durante el sprint.
> > > - Puede aumentar en función del tamaño de las tareas.
> 
> ## Kanban Board
> 
> > Es el tablero que muestra el flujo de trabajo de las tareas del sprint.
> > > - Contiene los elementos del Sprint Backlog.
> > > - Está organizado en etapas de acuerdo al nivel de progreso.
> 
> ## Página del equipo
> 
> > Se crea una página en Notion del equipo de trabajo:
> > > - Contiene las herramientas antes mencionadas.
> > > - Facilita la creación de apuntes en colaboración.
> > > [Enlace página](https://duvanroar.notion.site/DataDiip-8f3a971c346a4525986b5b782c500bf1?pvs=74)
> 
> ## Repositorio GitHub
> 
> > Se crea el repositorio de GitHub para facilitar la colaboración en el desarrollo del proyecto.
> > - Contiene toda la documentación del proyecto.
> > - Se crean ramas para cada uno de los integrantes del grupo.
> > - Se define un GitManager que republicará los cambios y aceptará los pull requests.


# PROYECTO FINAL DATA SCIENCE
**---**
FOTO DATADIIP Y TAXIS
## INTRODUCCIÓN Y CONTEXTO NYC
>La ciudad de Nueva York ha tenido un crecimiento acelerado en las últimas décadas, la que cuenta con más de 8 millones de habitantes en su zona urbana y más de **22 millones de habitantes en la zona metropolitana**. A su vez, cuenta con una densidad de **10.756 habitantes por kilometro cuadrado** según fuentes oficiales. Debido a esto, los desafíos que enfrenta en términos de transporte son importantes. En promedio una persona gasta más de **40 minutos para llegar a su trabajo** y su sistema de transporte cuenta con opciones como el metro, autobuses, bicicleta y taxis que están regulados por la **Comisión de Taxis y Limosinas (TLC)** y el **Departamento de Transporte de la Ciudad de Nueva York (DOT)**.

Una empresa de servicios de transporte de pasajeros, que actualmente se encuentra operando en el sector de micros de media y larga distancia, **está interesada en invertir en el sector de transporte de pasajeros con automóviles en Nueva York**. Con una visión de un futuro menos contaminado y ajustarse a las tendencias de mercado actuales, quieren, además de investigar la rentabilidad del negocio, verificar la relación entre este tipo de transporte y la calidad del aire, así como otras externalidades. Esto, con la finalidad de estudiar la posibilidad de implementar vehículos eléctricos a su flota; ya sea en su totalidad o parte de la misma.

​Debido a que se trataría de una unidad de negocio nueva, **se pretende hacer un análisis preliminar del movimiento de los taxis en la ciudad de Nueva York**, para tener un marco de referencia y poder tomar decisiones justificadas.

## PROPUESTA DE TRABAJO
Recopilar, depurar y disponibilizar la información: **Creación de una base de datos (DataWarehouse)** con información proveniente de diferentes fuentes, corriendo en local o alojada en proveedores en la nube. La base de datos depurada **deberá contemplar por lo menos dos tipos diferentes de extracción de datos**, como datos estáticos, llamadas a una API, scrapping, entre otros. 
El análisis **debe contemplar las relaciones entre variables** y concluir, si es que hubiera, una relación entre estas, y los posibles factores que pueden ocasionar dicha relación.
Por último, **se deberá generar un modelo de machine learning** de clasificación supervisado o no supervisado, entrenado y puesto en producción: Este modelo deberá resolver un problema y conectar globalmente con los objetivos propuestos.

## PROCEDIMIENTO

## 1. EXTRACCIÓN
Se identificaron fuentes de datos relevantes para el estudio y se obtuvieron ya sea de forma manual o mediante webscrapping (extracción de forma automatizada), una cantidad relevante de datasets para su posterior análisis.

## 2. ANÁLISIS EXPLORATORIO DE DATOS (EDA), TRANSFORMACIÓN Y LIMPIEZA
En este punto, se procedió a limpiar y preprocesar los datos extraídos para eliminar aquellos que tienden a estar fuera de rango (outliers), registros que están duplicados, datos incorrectos y/o faltantes, y así formatearlos según sea necesario.

## 3. CARGA
Al trabajar con grandes volúmenes de registros, es necesario cargar y almacenar los datos generados en la nube, mediante una herramienta de Datawarehouse o Datalake, ya que estos otorgan características importantes para el trabajo con datos, como lo son almacenamiento, seguridad y organización (muy importante en el primer caso).

## 4. ANÁLISIS DE DATOS Y MODELO DE MACHINE LEARNING
Una vez realizados los pasos anteriores, se procedió de manera paralela a analizar y visualizar los datos obtenidos y a generar un modelo de Machine Learning (ML) que responda a los objetivos planteados. Para el primer caso, se exploraron e identificaron tendencias y se monitorearon métricas clave o indicadores de rendimiento (KPIs) para poder tomar decisiones informadas respecto al propósito del proyecto. A su vez, la creación del modelo de ML tuvo como objetivo generar predicciones de demanda de vehículos en los diferentes sectores de Nueva York. 

### DASHBOARD
[![Dashboard.png](https://i.postimg.cc/mDQQ8Ynm/Dashboard.png)](https://postimg.cc/yg8gNZsR)

## MODELO MACHINE LEARNING
[![ML.png](https://i.postimg.cc/7hXXnFtH/ML.png)](https://postimg.cc/SY2Wyvp3)


## 5. DEPLOY EN LA WEB DE LOS RESULTADOS OBTENIDOS
Se creó una página web donde se presentan los principales resultados de este estudio.

### STREAMLIT
[![streamlit.png](https://i.postimg.cc/65qK794j/streamlit.png)](https://postimg.cc/PNg99n4Y)

### CALCULADORA DE VIAJE
[![Calculadora-Viaje.png](https://i.postimg.cc/d0mH4N0x/Calculadora-Viaje.png)](https://postimg.cc/VSvWNRnq)
.
