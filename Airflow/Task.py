from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello from Airflow!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    dag_id='sample_hello_dag_From_Windows',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval=None,  # Trigger manually
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello
    )
