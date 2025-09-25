from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from util import mounts, environment, security, volumes

with DAG(
        "argo_example",
        schedule="* * * * *",
        start_date=datetime.today(),
        catchup=False
) as dag:
    list_argo = KubernetesPodOperator(
        name="list-argo",
        task_id="list-argo",
        image="ghcr.io/euroargodev/coriolis-data-processing-chain-for-argo-floats-container:066a",
        cmds=["sh", "-c"],
        arguments=["ls -lsarth /users/argo"],
        env_vars=environment.default,
        container_security_context=security.devargo,
        volumes=[volumes.argo],
        volume_mounts=[mounts.argo]
    )

    list_devargo = KubernetesPodOperator(
        name="list-devargo",
        task_id="list-devargo",
        image="ghcr.io/euroargodev/coriolis-data-processing-chain-for-argo-floats-container:066a",
        cmds=["sh", "-c"],
        arguments=["ls -lsarth /users/devargo"],
        env_vars=environment.default,
        container_security_context=security.devargo,
        volumes=[volumes.devargo],
        volume_mounts=[mounts.devargo]
    )

    write_amrit = KubernetesPodOperator(
        name="write-amrit",
        task_id="write_amrit",
        image="ghcr.io/euroargodev/coriolis-data-processing-chain-for-argo-floats-container:066a",
        cmds=["sh", "-c"],
        arguments=["date > /users/devargo/amrit/hello-from-airflow.txt"],
        container_security_context=security.devargo,
        volumes=[volumes.devargo],
        volume_mounts=[mounts.devargo]
    )

    call_matlab = KubernetesPodOperator(
        name="call-matlab",
        task_id="call_matlab",
        image="ghcr.io/euroargodev/coriolis-data-processing-chain-for-argo-floats-container:066a",
        cmds=[
            "/lmod/modules/apps/matlab/2024b/bin/matlab",
            "-nodesktop",
            "-nodisplay",
            "-batch"
        ],
        arguments=["version"],
        env_vars=environment.default,
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

    list_argo >> list_devargo >> write_amrit >> call_matlab
