# Proyecto Final de Data Science

## Introducción y Contexto de la Ciudad de Nueva York

Nueva York ha experimentado un crecimiento acelerado en las últimas décadas, con más de 8 millones de habitantes en su zona urbana y más de 22 millones en la zona metropolitana. Esto ha resultado en una densidad poblacional de 10,756 habitantes por kilómetro cuadrado. Dada esta densidad y el constante flujo de personas, los desafíos en términos de transporte son significativos. El tiempo promedio de viaje para llegar al trabajo supera los 40 minutos, y las opciones de transporte incluyen el metro, autobuses, bicicletas y taxis, todos regulados por la Comisión de Taxis y Limusinas (TLC) y el Departamento de Transporte de la Ciudad de Nueva York (DOT).

Una empresa de servicios de transporte de pasajeros, actualmente operando en el sector de micros de media y larga distancia, está interesada en invertir en el sector de transporte de pasajeros con automóviles en Nueva York. Con una visión de un futuro menos contaminado y en línea con las tendencias de mercado actuales, la empresa busca investigar la rentabilidad del negocio y verificar la relación entre este tipo de transporte y la calidad del aire, entre otras externalidades. Esto implica estudiar la viabilidad de implementar vehículos eléctricos en su flota, ya sea en su totalidad o en parte.

Dado que esta sería una nueva unidad de negocio, se propone realizar un análisis preliminar del movimiento de los taxis en la ciudad de Nueva York para tener un marco de referencia y tomar decisiones fundamentadas.

## Objetivos del Proyecto

- Recopilar, depurar y disponibilizar información relevante para el análisis.
- Realizar un análisis exploratorio de datos para identificar patrones y tendencias.
- Crear modelos de Machine Learning para predecir la demanda de vehículos en diferentes sectores de Nueva York.
- Desarrollar una infraestructura de MLOps mixta utilizando módulos y scripts locales, así como automatización en la nube.
- Desarrollar MVPs interactivos para presentar los resultados del análisis en Streamlit, Power BI y en una plataforma web.<br>
Para mayor comprención del modelo de datos [Documentacion](https://github.com/clblommberg/MVP_ML_TransporteNY/blob/main/Documentacion.md)

## Stack Tecnológico y Recursos Utilizados

| Tecnologías Utilizadas     | Recursos Min. Utilizados                           |
|---------------------------|-----------------------------------------------|
| Python 3.10.11                | Sistema Operativo: Windows                    |
| Pandas                    | Memoria RAM: 16 GB                            |
| Dask                      | CPU: 4 núcleos                                |
| Scikit-learn              |                                                |
| Azure Synapse             |                                               |
| Azure Data Lake Storage   |                                               |


## Metodología

El proyecto se llevará a cabo planificación [Scrumban](https://github.com/clblommberg/MVP_ML_TransporteNY/blob/main/Scrumban.md) y en las siguientes etapas en el proceso de desarrollo:

1. **Recopilación y Depuración de Información**: Se recopilarán datos de diversas fuentes y se limpiarán para eliminar duplicados, outliers y datos incorrectos.

2. **Análisis Exploratorio de Datos (EDA)**: Se explorarán los datos para identificar patrones, tendencias y relaciones entre variables.

3. **Modelado de Machine Learning**: Se desarrollarán modelos predictivos utilizando técnicas de Machine Learning para predecir la demanda de vehículos.

4. **Desarrollar una infraestructura de MLOps**: Se establecerá una infraestructura de MLOps para gestionar y automatizar el ciclo de vida de los modelos, incluyendo la implementación, monitoreo y actualización de los mismos.

5. **Desarrollar MVPs interactivos**: Se crearán MVPs interactivos, como dashboards en Streamlit, Power BI y una plataforma web, para visualizar y comunicar los resultados del análisis de datos y los modelos de Machine Learning.

<style>
    img {
        width: 600px;
        height: 300px;
    }
</style>

### Dashboard Powe BI
[![Dashboard.png](https://i.postimg.cc/mDQQ8Ynm/Dashboard.png)](https://postimg.cc/yg8gNZsR)

### Streamlit
[![ML.png](https://i.postimg.cc/7hXXnFtH/ML.png)](https://postimg.cc/SY2Wyvp3)

[![streamlit.png](https://i.postimg.cc/65qK794j/streamlit.png)](https://postimg.cc/PNg99n4Y)

### WebAPP 
[![Calculadora-Viaje.png](https://i.postimg.cc/d0mH4N0x/Calculadora-Viaje.png)](https://postimg.cc/VSvWNRnq)


## Conclusiones

El análisis preliminar del movimiento de los taxis en la ciudad de Nueva York proporciona una visión general del estado actual del transporte de pasajeros en la ciudad. Los modelos de Machine Learning desarrollados permiten predecir la demanda de vehículos en diferentes sectores de Nueva York, lo que puede ser útil para la toma de decisiones en la futura inversión en el sector de transporte de pasajeros con automóviles.
