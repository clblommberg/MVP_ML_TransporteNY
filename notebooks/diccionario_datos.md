![DiccionarioDatos](public/v15.jpg)
---
`Bienvenido al notebook dedicado a la creación de un diccionario de datos para nuestro proyecto. Este diccionario de datos proporciona una descripción detallada de los conjuntos de datos utilizados en nuestro proyecto, incluyendo información sobre las características presentes en cada conjunto de datos, así como sus tipos de datos y una explicación de su significado.`

`Un diccionario de datos bien definido es esencial para comprender la estructura y el contenido de nuestros datos, lo que facilita su análisis y la toma de decisiones informadas. En este notebook, exploraremos cada conjunto de datos utilizado en nuestro proyecto y crearemos un diccionario de datos completo que servirá como referencia útil durante todo el proceso de análisis y modelado de datos. ¡Comencemos este viaje para comprender mejor nuestros datos y desbloquear su potencial!`

![TA](public/v14.jpg)
### **Nombre de la base de datos: TaxisAmarillos** ###
---

**Descripción:**

>*La base de datos proporciona un registro de viajes realizados en taxis amarillos en la ciudad de Nueva York entre los años 2022 y 2023. Esta base de datos no solo proporciona una instantánea detallada de la actividad de los taxis amarillos en la ciudad, sino que también sirve como una herramienta fundamental para comprender los patrones de movilidad urbana y los hábitos de viaje de los residentes y visitantes de Nueva York.*

**Tamaño:**

>*Tamaño de la base de datos*

**DBMS**

>*Azure*

**Variables**

>*A continuación se relacionan cada una de las variables de esta base de datos que proporcionan una visión global de la estructura y las características del conjunto de datos:*

| Nombre de la columna | Descripción de la columna                                                                                             | Valores ejemplo                    | Tipo de Dato (Py) | Tipo de Variable    | Llave    |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:-----------------:|:-------------------:|:--------:|
| IdProveedor          | Identificador único del proveedor de servicios que se encuentra registrado en la base de datos de TPEP.               | 1 = "Creative Mobile Technologies" | Integer           | Categórica(nominal) | Foránea |
| IdZonaOrigen         | Identificador único de la zona de la ciudad desde la que se inicia el viaje a través de la activación del taxímetro.  | 2 = "Jamaica Bay"                  | Integer           | Categórica(nominal) | Foránea  |
| IdZonaDestino        | Identificador único de la zona de la ciudad en la que se finaliza el viaje.                                           | 4 = "Alphabet City"                | Integer           | Categórica(nominal) | Foránea  |
| FechaRecogida        | Fecha en formato (YYY-MM-DD) en la cual el taxi llegó a recoger al pasajero.                                          | 2022-04-05                         | Date              | Categórica(nominal) | -------- |
| HoraRecogida         | Hora en formato (24 horas) en la cual el taxi llegó a recoger al pasajero **Nota**: No incluye minutos, solo la  hora.| 18 (6 PM)                          | Integer           | Categórica(nominal) | -------- |
| DuracionViaje        | Duración total del viaje en segundos desde que se inició el viaje en el taxímetro hasta el destino final del pasajero.| 1200 (20 minutos)                  | Integer           | Numérica(discreta)  | -------- |
| DistanciaViaje       | Cantidad total de millas recorridas desde que se inició el viaje hasta que se finalizó.                               | 5.4 (Millas)                       | Float             | Numérica(continua)  | -------- |
| TotalPasajeros       | Cantidad total de pasajeros movilizados en el viaje.                                                                  | 3                                  | Integer           | Numérica(discreta)  | -------- |
| TipoTarifa           | Tipo de tarifa cobrada en el viaje, de acuerdo a la regulación de tarifas por Comisión de Limosinas y Taxis.          | 2 = Aeroportuaria (JFK)            | Integer           | Catégorica(nominal) | Foránea  |
| TipoPago             | Medio de pago que usó el pasajero para costear el precio del viaje.                                                   | 1 = Tarjeta de Crédito             | Integer           | Catégorica(nominal) | Foránea  |
| CostoTotal           | Costo total del viaje en dólares (USD), incluídos impuestos, sobrecargos y peajes.                                    | 17.5                               | Float             | Numérica(continua)  | -------- |


![TF](public/v17.jpg)
### **Nombre de la base de datos: TaxisHFVH** ###
---

**Descripción:**

>*La base de datos proporciona un registro de viajes realizados en taxis tipo vehículo de alquiler con conductor en la ciudad de Nueva York entre los años 2022 y 2023. Esta base de datos no solo proporciona una instantánea detallada de la actividad de este modelo de servicio en la ciudad, sino que también sirve como una herramienta fundamental para comprender los patrones de movilidad urbana y los hábitos de viaje de los residentes y visitantes de Nueva York, así como comparar el impacto de este modelo de servicio con el impacto del modelo de taxis tradicionales (amarillos).*

**Tamaño:**

>*Tamaño de la base de datos*

**DBMS**

>*Azure*

**Variables**

>*A continuación se relacionan cada una de las variables de esta base de datos que proporcionan una visión global de la estructura y las características del conjunto de datos:*

| Nombre de la columna | Descripción de la columna                                                                                             | Valores ejemplo                    | Tipo de Dato (Py) | Tipo de Variable    | Llave    |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:-----------------:|:-------------------:|:--------:|
| IdPlataforma         | Identificador único de la plataforma digital que gestiona los viajes por aplicación.                                  | 3 = Uber                           | Integer           | Categórica(nominal) | Foránea |
| IdProveedor          | Identificador único del proveedor de servicios que se encuentra registrado en la base de datos de TPEP.               | 1 = "Creative Mobile Technologies" | Integer           | Categórica(nominal) | Foránea |
| IdZonaOrigen         | Identificador único de la zona de la ciudad desde la que se inicia el viaje a través de la activación del taxímetro.  | 2 = "Jamaica Bay"                  | Integer           | Categórica(nominal) | Foránea  |
| IdZonaDestino        | Identificador único de la zona de la ciudad en la que se finaliza el viaje.                                           | 4 = "Alphabet City"                | Integer           | Categórica(nominal) | Foránea  |
| FechaRecogida        | Fecha en formato (YYY-MM-DD) en la cual el taxi llegó a recoger al pasajero.                                          | 2022-04-05                         | Date              | Categórica(nominal) | -------- |
| TiempoRecogida       | Tiempo en segundos que se demoró el vehículo en llegar al punto de recogida del pasajero, desde que se solicitó.      | 2022-04-05                         | Date              | Categórica(nominal) | -------- |
| HoraRecogida         | Hora en formato (24 horas) en la cual el taxi llegó a recoger al pasajero **Nota**: No incluye minutos, solo la  hora.| 18 (6 PM)                          | Integer           | Categórica(nominal) | -------- |
| DuracionViaje        | Duración total del viaje en segundos desde que se inició el viaje en la aplicación hasta el destino final.            | 1200 (20 minutos)                  | Integer           | Numérica(discreta)  | -------- |
| DistanciaViaje       | Cantidad total de millas recorridas desde que se inició el viaje hasta que se finalizó.                               | 5.4 (Millas)                       | Float             | Numérica(continua)  | -------- |
| CostoTotal           | Costo total del viaje en dólares (USD), incluídos impuestos, sobrecargos y peajes.                                    | 17.5                               | Float             | Numérica(continua)  | -------- |


![EC](public/v16.jpg)
### **Nombre de la base de datos:** EmisionesCO2 ###
---

**Descripción:**

>*La base de datos proporciona un registro de las emisiones de dióxido de carbono (CO2) en Estados Unidos en un extenso periodo entre 1980 y 2020, recopilada a partir de datos de la Administración de Energía de los Estados Unidos. Esta base de datos proporciona una perspectiva histórica sobre las tendencias de las emisiones de CO2 y su relación con la actividad económica y la población de este país.*

**Tamaño:**

>*Tamaño de la base de datos*

**DBMS**

>*Azure*

**Variables**

>*A continuación se relacionan cada una de las variables de esta base de datos que proporcionan una visión global de la estructura y las características del conjunto de datos:*

| Nombre de la columna | Descripción de la columna                                                                                             | Valores ejemplo                    | Tipo de Dato (Py) | Tipo de Variable    | Llave    |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:-----------------:|:-------------------:|:--------:|
| Año                  | Año en el que se registraron las mediciones de dióxido de carbono (AAAA).                                             | 1990                               | Integer           | Categórica(nominal) | -------- |
| TipoEnergia          | Tipo de fuente para producir las energía.                                                                             | "Renovable" / "No Renovable"       | String            | Categórica(nominal) | -------- |
| ProduccionEnergia    | Cantidad total de energía producida por el país (Joules).                                                             | 34.15                              | Float             | Numérica(continua)  | -------- |
| ConsumoEnergia       | Cantidad total de energía consumida por el país (Joules).                                                             | 20.47                              | Float             | Numérica(continua)  | -------- |
| Poblacion            | Cantidad total de personas en el país.                                                                                | 227119000                          | Integer           | Numérica(discreta)  | -------- |
| ConsumoPerCapita     | Consumo de energía por habitante del país . Consumo Energía / Población                                               | 10.1                               | Float             | Numérica(continua)  | -------- |
| TotalEmisionesCO2    | Cantidad total de dióxido de carbono (CO2) emitido en millones de toneladas                                           | 2455.15                            | Float             | Numérica(continua)  | -------- |



![CA](public/v11.jpg)
### **Nombre de las bases de datos:** CalidadAireNYC, CalidadAireBor, CalidadAireDC ###
---

**Descripción:**

>*Las base de datos proporcionan información sobre la calidad del aire en la ciudad de Nueva York, muy importante considerando las amenazas ambientales que genera la contaminación ambiental en las poblaciones urbanas. Esta base de datos permite observar los niveles de exposición y la vulnerabilidad de la población en diferentes escalas de la ciudad, y así determinar focos en donde se podrían implementar medidas para reducir estos niveles. Estos indicadores proporcionan una perspectiva a lo largo del tiempo y de las geografías de Nueva York para caracterizar mejor la calidad del aire y sus efectos en la salud.*

**Tamaño:**

>*Tamaño de las base de datos*

**Fuente**

>[EnvironmentData](http://nyc.gov/health/environmentdata)

**DBMS**

>*Azure*

**Variables**

>*A continuación se relacionan cada una de las variables de esta base de datos que proporcionan una visión global de la estructura y las características del conjunto de datos:*

| Nombre de la columna | Descripción de la columna                                                                                             | Valores ejemplo                    | Tipo de Dato (Py) | Tipo de Variable    | Llave    |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:-----------------:|:-------------------:|:--------:|
| IdBorough / IdDC     | Identificador único del lugar donde se tomó la medición (Borough, Distrito Comunitario).                              | 1 = Manhattan                      | Integer           | Categórica(nominal) | Foránea  |
| FechaInicio          | Determina la fecha en la cual se empezó la medición de la calidad del aire, en formato: YYYY-MM-DD                    | 2019-01-01                         | Date              | Categórica(ordinal) | -------- |
| PeriodoTiempo        | Determina el intervalo de tiempo en el que se hizo la medición, ya sea anual o semestral (Año, Verano, Invierno)      | "Año"                              | String            | Categórica(nominal) | -------- |
| Contaminante         | Determina la particula que se midió en la calidad del aire (Dióxido de Nitrógeno, Ozono, Material Particulado)        | "NO2"                              | String            | Categórica(nominal) | -------- |
| mcg/m3               | Concentración total de particulas medido en microgramos por metro cúbico.                                             | 31.96                              | Float             | Numérica(continua)  | -------- |




![VG](public/v18.jpg)
### **Nombre de la base de datos:** VehiculosCombustion ###
---

**Descripción:**

>*Las base de datos proporciona información que le permite a los compradores de autos tomar decisiones informadas y hacer comparaciones sobre el consumo de combustible de cada uno de los vehículos registrados en la base de datos. También, los datos permiten obtener información sobre el impacto ambiental de cada vehículo, a mayor combustible consume un vehículo más gases de efecto invernadero emite, entre ellos dióxido de carbono.*
>*Cada litro de gasolina utilizado contribuye con aproximadamente 2.3 kg de CO2.*

**Tamaño:**

>*Tamaño de la base de datos*

**Fuente**

>[FuelConsumptionsRating](https://natural-resources.canada.ca/energy-efficiency/transportation-alternative-fuels/fuel-consumption-guide/understanding-fuel-consumption-ratings/21006)

**DBMS**

>*Azure*

**Variables**

>*A continuación se relacionan cada una de las variables de esta base de datos que proporcionan una visión global de la estructura y las características del conjunto de datos:*

| Nombre de la columna | Descripción de la columna                                                                                             | Valores ejemplo                    | Tipo de Dato (Py) | Tipo de Variable    | Llave    |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:-----------------:|:-------------------:|:--------:|
| AñoModelo            | Año en el cual el modelo de vehículo fue lanzado al mercado                                                           | 2012                               | Integer           | Categórica(ordinal) | -------- |
| Fabricante           | Determina la compañía concesionaria que fabricó el vehículo                                                           | "Acura"                            | String            | Categórica(nominal) | -------- |
| Modelo               | Determina el nombre otorgado a la línea de vehículo que se fabricó y se comercializó.                                 | "ILX"                              | String            | Categórica(nominal) | -------- |
| Consumo              | Determina el consumo de combustible en galones por milla recorrida.                                                   | 0.9                                | Float             | Numérica(continua)  | -------- |
| EmisionesCO2         | Concentración total de particulas medido en gramos por milla.                                                         | 31.96                              | Float             | Numérica(continua)  | -------- |



![VG](public/v19.jpg)
### **Nombre de la base de datos:** VehiculosEléctricos ###
---

**Descripción:**

>*Las base de datos proporciona información que le permite a los compradores de autos eléctricos tomar decisiones informadas y hacer comparaciones sobre el consumo de energía de cada uno de los vehículos registrados en la base de datos. También, los datos permiten obtener información sobre el impacto ambiental de cada vehículo (si bien son electricos y no generan emisiones directas, se realiza una estimación de las emisiones indirectas por usar energía), a mayor kwh consume un vehículo más gases de efecto invernadero emite indirectamente.*

**Tamaño:**

>*Tamaño de la base de datos*

**Fuente**

>[Electrics](https://open.canada.ca/data/en/)

**DBMS**

>*Azure*

**Variables**

>*A continuación se relacionan cada una de las variables de esta base de datos que proporcionan una visión global de la estructura y las características del conjunto de datos:*

| Nombre de la columna | Descripción de la columna                                                                                             | Valores ejemplo                    | Tipo de Dato (Py) | Tipo de Variable    | Llave    |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------|:---------------------------------:|:-----------------:|:-------------------:|:--------:|
| AñoModelo            | Año en el cual el modelo de vehículo fue lanzado al mercado                                                           | 2012                               | Integer           | Categórica(ordinal) | -------- |
| Fabricante           | Determina la compañía concesionaria que fabricó el vehículo                                                           | "Acura"                            | String            | Categórica(nominal) | -------- |
| Modelo               | Determina el nombre otorgado a la línea de vehículo que se fabricó y se comercializó.                                 | "ILX"                              | String            | Categórica(nominal) | -------- |
| Consumo              | Determina el consumo de combustible en kwh por milla recorrida.                                                       | 0.9                                | Float             | Numérica(continua)  | -------- |
| EmisionesCO2         | Concentración total de particulas medido en gramos por milla.                                                         | 31.96                              | Float             | Numérica(continua)  | -------- |
| TiempoRecarga        | Cantidad de tiempo en horas que se necesitan para recargar el vehículo a un 100%.                                     | 9.5                                | Float             | Numérica(continua)  | -------- |