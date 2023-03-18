from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from etl_folder import extract
with DAG(
    dag_id='Project_with_AWS',
    default_args={
        'depends_on_past': False,
        'email': ['amonza621@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 5,
        'retry_delay': timedelta(minutes=5),
    },
    description= 'Proyecto creado con la intención de poner en práctica mis conocimientos con las herramientas de interés de AWS.',
    schedule_interval = '@daily',
    start_date = datetime(2023, 1, 25),
    catchup = False,
) as dag:
    t1 = PythonOperator(
        task_id ='extract_with_tweepy',
        python_callable= extract.extract
    )