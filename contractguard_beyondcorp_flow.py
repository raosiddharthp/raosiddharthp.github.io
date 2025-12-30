from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing, TrafficDirector
from diagrams.gcp.security import KeyManagementService, Iam
from diagrams.gcp.compute import Run
from diagrams.generic.device import Tablet

# TOGAF Phase D: Technology Architecture - Zero Trust Access
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "BeyondCorp Access Flow: Zero Trust EA", 
    show=False, 
    filename="contractguard_beyondcorp_flow", 
    direction="LR", 
    graph_attr=graph_attr
):
    user = Tablet("Remote Counsel\n(Managed Device)")

    with Cluster("Google Cloud Edge"):
        lb = LoadBalancing("Global HTTP(S) LB")
        iap = TrafficDirector("Identity-Aware Proxy\n(Context-Aware Access)")

    with Cluster("Identity & Governance"):
        iam = Iam("Cloud IAM\n(RBAC/ABAC)")
        context = Iam("Device Posture\nVerification")

    with Cluster("Protected Resource (ContractGuard)"):
        app = Run("Contract Analytics\nService")
        kms = KeyManagementService("KMS (Encryption)")

    # Defining the Secure Access Flow
    user >> Edge(label="HTTPS Request", color="darkblue") >> lb
    lb >> iap
    iap >> Edge(label="Verify Context", color="darkorange", style="dashed") >> [iam, context]
    iap >> Edge(label="Access Granted", color="darkgreen", style="bold") >> app
    app >> kms