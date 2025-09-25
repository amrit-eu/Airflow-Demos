from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client.models import V1Volume, V1PersistentVolumeClaimVolumeSource

__all__ = ["argo", "devargo", "modules"]

argo = V1Volume(
    name="argo",
    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
        claim_name="nocl-scale-bodc2-users-argo-airflow",
        read_only=True
    )
)

devargo = V1Volume(
    name="devargo",
    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
        claim_name="nocl-scale-bodc2-users-devargo-airflow",
        read_only=False
    )
)

modules = [
    V1Volume(
        name="module-apptainer",
        persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
            claim_name="nocl-module-apptainer-airflow",
            read_only=True
        )
    ),
    V1Volume(
        name="module-easybuild",
        persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
            claim_name="nocl-module-easybuild-airflow",
            read_only=True
        )
    ),
    V1Volume(
        name="module-lmod",
        persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
            claim_name="nocl-module-lmod-airflow",
            read_only=True
        )
    ),
    V1Volume(
        name="module-modulefiles",
        persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
            claim_name="nocl-module-modulefiles-airflow",
            read_only=True
        )
    ),
    V1Volume(
        name="module-modules",
        persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
            claim_name="nocl-module-modules-airflow",
            read_only=True
        )
    )
]
