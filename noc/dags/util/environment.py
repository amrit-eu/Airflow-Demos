from kubernetes.client.models import V1EnvVar

__all__ = ["DEFAULT"]

DEFAULT = [
    V1EnvVar(
        name="TZ",
        value="Europe/London"
    ),
    # Save wasting space on the MathWorks Service Host
    V1EnvVar(
        name="MATHWORKS_SERVICE_HOST_MANAGED_INSTALL_ROOT",
        value="/lmod/modules/apps/mathworks/2025_02_10/"
    ),
    # Register with the NOCL MATLAB licence server
    V1EnvVar(
        name="MLM_LICENSE_FILE",
        value="27000@livlic8.noc.ac.uk"
    )
]

DECODER = [
    V1EnvVar(
        name="MCRROOT",
        value="/lmod/modules/apps/matlab/2022b"
    )
]
