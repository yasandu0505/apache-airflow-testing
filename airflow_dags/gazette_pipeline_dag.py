from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'mock_user',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    dag_id='mock_gazette_pipeline',
    default_args=default_args,
    description='Mock DAG to simulate document archiving pipeline',
    schedule=None,  # Changed from schedule_interval to schedule
    start_date=datetime(2025, 7, 23),
    catchup=False,
    tags=['mock', 'gazette'],
) as dag:

    run_main = BashOperator(
        task_id='run_mock_main_py',
        bash_command='cd /Users/yasandu/apache-airflow-testing && python3 main.py --year 2023 --lang en'
    )