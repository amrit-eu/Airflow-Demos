from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from .util import mounts, environment, security, volumes

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
        arguments=["echo Hello World"],
        container_security_context=security.devargo,
        task_id="pod_hello"
    )
    say_goodbye = KubernetesPodOperator(
        name="goodbye-pod",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo Goodbye World"],
        container_security_context=security.devargo,
        task_id="pod_goodbye"
    )
    list_files = KubernetesPodOperator(
        name="list-files",
        task_id="list_files",
        image="ghcr.io/euroargodev/coriolis-data-processing-chain-for-argo-floats-container:066a",
        cmds=[
            "/lmod/modules/apps/matlab/2024b/bin/matlab",
            "-nodesktop",
            "-nodisplay",
            "-batch"
        ],
        arguments=["version"],
        env_vars=environment.nocl_matlab,
        container_security_context=security.devargo,
        volumes=[
            volumes.argo,
            volumes.devargo,
            *volumes.modules
        ],
        volume_mounts=[
            mounts.argo,
            mounts.devargo,
            *mounts.modules
        ]
    )

    say_hello >> say_goodbye >> list_files
