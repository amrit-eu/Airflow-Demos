from airflow import DAG
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator


with DAG(
        "argo_hello",
        schedule="* * * * *",
        start_date=datetime.today(),
        catchup=False
) as dag:
    say_hello = KubernetesPodOperator(
        name="hello-pod",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo", "Hello World!"],
        task_id="pod_hello"
    )
    say_goodbye = KubernetesPodOperator(
        name="goodbye-pod",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo", "Goodbye World!"],
        task_id="pod_goodbye"
    )

    say_hello >> say_goodbye
