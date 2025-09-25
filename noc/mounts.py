from kubernetes.client.models import V1VolumeMount

argo = V1VolumeMount(
    name="argo",
    mount_path="/users/argo",
    read_only=True
)

devargo = V1VolumeMount(
    name="devargo",
    mount_path="/users/devargo",
    read_only=True
)
devargo_amrit = V1VolumeMount(
    name="devargo",
    sub_path="amrit",
    mount_path="/amrit",
    read_only=False
)

modules = [
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
