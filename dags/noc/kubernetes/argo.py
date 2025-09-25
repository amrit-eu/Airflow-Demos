from airflow import DAG
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client.models import V1VolumeMount, V1Volume, V1PersistentVolumeClaimSource




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
        task_id="pod_hello"
    )
    say_goodbye = KubernetesPodOperator(
        name="goodbye-pod",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo Goodbye World"],
        task_id="pod_goodbye"
    )
    list_files = KubernetesPodOperator(
        name="list-files",
        task_id="list_files",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["ls -lsarth /users/devargo"],
        security_context={
            "privileged": False,
            "capabilities": {
                "drop": ["ALL"]
            }
        },
        volumes=[
            V1Volume(
                name="devargo",
                persistent_volume_claim=PersistentVolumeClaimVolumeSource(
                    claim_name="nocl-scale-bodc2-users-devargo-airflow",
                    read_only=True
                )
            )
        ],
        volume_mounts=[
            V1VolumeMount(
                name="devargo",
                mount_path="/users/devargo",
                read_only=True
            )
        ]
    )

    say_hello >> say_goodbye >> list_files
