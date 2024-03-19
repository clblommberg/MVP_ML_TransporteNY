import pandas as pd
import plotly.express as px

# Datos actualizados con etiquetas adicionales
data = {
    'Tarea': ['Exploración y Planificación de Estrategia', 
              'Presentación de Propuesta y Asignación Roles en Git para ML y DevOps.', 
              'Comprensión de la situación actual', 
              'Planteo de KPIs', 
              'Reformulación de Estrategia y Planificación', 
              'EDA Previo', 
              'Stack Técnologico', 
              'Objetivos y alcance', 
              'EDA Final', 
              'Modelo Relacional en DW', 
              'ETL Documentacion', 
              'EDA Final Interpretación', 
              'Automatización con Airflow', 
              'Semana Santa', 
              'Plazo de entrega', 
              'Reportes/Dashboards', 
              'KPI', 
              'Modelos de ML', 
              'Proyecto a Producción'],
    'Etiqueta': ['Claudio', 'Grupo', 'Sebastian-Issac', 'Byron-Duvan', 'Grupo', 'Claudio', 'Grupo', 'Grupo',
                 'Byron-Duvan', 'Claudio', 'Sebastian-Issac', 'Byron-Duvan', 'Claudio', 'Henry', 'Henry',
                 'Duvan-Herlin', 'Sebastian', 'Claudio - Byron', 'Claudio'],
    'Inicio': ['2024-03-18', '2024-03-19', '2024-03-19', '2024-03-19', '2024-03-19', '2024-03-19', '2024-03-19', 
               '2024-03-19', '2024-03-22', '2024-03-22', '2024-03-24', '2024-03-24', '2024-03-25', '2024-03-25', 
               '2024-04-01', '2024-04-01', '2024-04-01', '2024-04-01', '2024-04-07'],
    'Fin': ['2024-03-19', '2024-03-19', '2024-03-20', '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-22', 
            '2024-03-22', '2024-03-24', '2024-03-25', '2024-03-25', '2024-03-25', '2024-03-27', '2024-03-29', 
            '2024-04-22', '2024-04-07', '2024-04-07', '2024-04-07', '2024-04-14']
}

df2 = pd.DataFrame(data)
# Ruta al archivo ODS
ruta_archivo = 'gantt.ods'

# Leer el archivo ODS en un DataFrame de Pandas
df = pd.read_excel(ruta_archivo, engine='odf')


# Convertir las columnas de fecha a tipo datetime
df['Inicio'] = pd.to_datetime(df['Inicio'])
df['Fin'] = pd.to_datetime(df['Fin'])

# Crear el gráfico Gantt con Plotly
fig = px.timeline(df, x_start='Inicio', x_end='Fin', y='Tarea', title='Diagrama de Gantt - Proyecto XYZ',
                  labels={'Inicio': 'Fecha de inicio', 'Fin': 'Fecha de fin', 'Tarea': 'Tarea'},
                  color='Etiqueta', 
                  hover_name='Tarea',
                  color_discrete_sequence=px.colors.qualitative.Dark24)

# Personalizar el eje x para mostrar solo los meses y el año
fig.update_layout(xaxis_tickformat='%b\n%Y')

# Mostrar el gráfico
fig.show()