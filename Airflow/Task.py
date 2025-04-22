from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import time
import sys
import shutil
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Multi_thread import thread


def Scrape_Job():
    start = time.time()
    print("Chrome path:", shutil.which("google-chrome"))
    print("Driver path:", shutil.which("chromedriver"))
    print("Starting the Job!")
    thread()
    end = time.time()
    print(f"Completed the Job in {end - start:.4f} seconds")


default_args = {
    'owner': 'Gokul',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    dag_id='extraction_job',
    default_args=default_args,
    description='DAG for Extracting jobs',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='extraction_job',
        python_callable=Scrape_Job
    )
