from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from util import mounts, environment, security, volumes, images

with DAG(
        "argo_example",
        schedule="* * * * *",
        start_date=datetime.today(),
        catchup=False
) as dag:
    list_argo = KubernetesPodOperator(
        name="list-argo",
        task_id="list-argo",
        image=images.DECODER,
        cmds=["bash", "-xec"],
        arguments=["ls -lsarth /users/argo"],
        env_vars=environment.DEFAULT,
        container_security_context=security.DEVARGO,
        volumes=[volumes.ARGO],
        volume_mounts=[mounts.ARGO]
    )

    list_devargo = KubernetesPodOperator(
        name="list-devargo",
        task_id="list-devargo",
        image=images.DECODER,
        cmds=["bash", "-xec"],
        arguments=["ls -lsarth /users/devargo"],
        env_vars=environment.DEFAULT,
        container_security_context=security.DEVARGO,
        volumes=[volumes.DEVARGO],
        volume_mounts=[mounts.DEVARGO]
    )

    write_amrit = KubernetesPodOperator(
        name="write-amrit",
        task_id="write_amrit",
        image=images.DECODER,
        cmds=["bash", "-xec"],
        arguments=["date > /users/devargo/amrit/hello-from-airflow.txt"],
        container_security_context=security.DEVARGO,
        volumes=[volumes.DEVARGO],
        volume_mounts=[mounts.DEVARGO]
    )

    read_amrit = KubernetesPodOperator(
        name="read-amrit",
        task_id="read_amrit",
        image=images.DECODER,
        cmds=["bash", "-xec"],
        arguments=["cat /users/devargo/amrit/hello-from-airflow.txt"],
        container_security_context=security.DEVARGO,
        volumes=[volumes.DEVARGO],
        volume_mounts=[mounts.DEVARGO]
    )

    list_runtime = KubernetesPodOperator(
        name="list-runtime",
        task_id="list_runtime",
        image=images.DECODER,
        cmds=["bash", "-xec"],
        arguments=["ls -lsarth ${MCRROOT}/*"],
        env_vars=environment.DEFAULT + environment.DECODER,
        container_security_context=security.DEVARGO,
        volumes=volumes.MODULES,
        volume_mounts=mounts.MODULES
    )

    call_matlab = KubernetesPodOperator(
        name="call-matlab",
        task_id="call_matlab",
        image=images.DECODER,
        cmds=[
            "/lmod/modules/apps/matlab/2024b/bin/matlab",
            "-nodesktop",
            "-nodisplay",
            "-batch"
        ],
        arguments=["version"],
        env_vars=environment.DEFAULT + environment.DECODER,
        container_security_context=security.DEVARGO,
        volumes=volumes.MODULES,
        volume_mounts=mounts.MODULES
    )

    call_decoder = KubernetesPodOperator(
        name="call-decoder",
        task_id="call_decoder",
        image=images.DECODER,
        cmds=[
            "python3",
            "-u",
            "/app/decoder_bindings/main.py"
        ],
        arguments=["version"],
        env_vars=environment.DEFAULT + environment.DECODER,
        container_security_context=security.DEVARGO,
        volumes=[volumes.DEVARGO] + volumes.MODULES,
        volume_mounts=[mounts.ADEVRGO] + mounts.MODULES
    )

    list_argo >> list_devargo >> write_amrit >> read_amrit
    list_argo >> list_runtime >> call_matlab
