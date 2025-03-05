from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def greet():
    print("Hello from Airflow! This is a sample DAG.")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email': ['admin@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG for local Airflow setup',
    schedule_interval=timedelta(days=1),
)

# Define a task using the PythonOperator
greet_task = PythonOperator(
    task_id='greet',
    python_callable=greet,
    dag=dag,
)

greet_task
