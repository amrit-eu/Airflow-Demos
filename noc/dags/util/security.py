from kubernetes.client.models import V1SecurityContext, V1Capabilities

__all__ = ["DEVARGO"]

DEVARGO = V1SecurityContext(
    allow_privilege_escalation=False,
    capabilities=V1Capabilities(
        drop=["ALL"]
    ),
    privileged=False,
    run_as_non_root=True,
    run_as_user=18685,
    run_as_group=18002
)
