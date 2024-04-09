from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os

def print_system_info(**kwargs):
    current_dir = os.getcwd()
    print(f"El directorio actual es: {current_dir}")
    print(f"El sistema operativo es: {os.name}")

with DAG(
    dag_id="ejemplo_dag",
    description="Un DAG de ejemplo",
    start_date=datetime(2023, 4, 8),
    schedule_interval=None  # Se ejecuta una sola vez
) as dag:

    tarea_1 = PythonOperator(
        task_id="imprimir_info_sistema",
        python_callable=print_system_info
    )

    tarea_1