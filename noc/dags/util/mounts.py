from kubernetes.client.models import V1VolumeMount

__all__ = ["ARGO", "DEVARGO", "MODULES"]

ARGO = V1VolumeMount(
    name="argo",
    mount_path="/users/argo",
    read_only=True
)

DEVARGO = V1VolumeMount(
    name="devargo",
    mount_path="/users/devargo",
    read_only=False
)

MODULES = [
    V1VolumeMount(
        name="module-apptainer",
        mount_path="/apptainer",
        read_only=True
    ),
    V1VolumeMount(
        name="module-easybuild",
        mount_path="/lmod/easybuild",
        read_only=True
    ),
    V1VolumeMount(
        name="module-lmod",
        mount_path="/lmod/lmod",
        read_only=True
    ),
    V1VolumeMount(
        name="module-modulefiles",
        mount_path="/lmod/modulefiles",
        read_only=True
    ),
    V1VolumeMount(
        name="module-modules",
        mount_path="/lmod/modules",
        read_only=True
    )
]
