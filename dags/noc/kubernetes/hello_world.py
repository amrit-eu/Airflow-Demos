from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello World! This is Airflow running on Kubernetes :)")

def goodbye():
    print("Goodbye World!")

def reply():
    print("Hello yourself!")

with DAG(
        "matcaz_hello",
        schedule="* * * * *",
        start_date=datetime.today(),
        catchup=False
) as dag:
    say_hello = PythonOperator(
        task_id="say_hello",
        python_callable=hello
    )
    say_goodbye = PythonOperator(
        task_id="say_goodbye",
        python_callable=goodbye
    )
    say_reply = PythonOperator(
        task_id="say_reply",
        python_callable=reply
    )

    say_hello >> say_reply >> say_goodbye
