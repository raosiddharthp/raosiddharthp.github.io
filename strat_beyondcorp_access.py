from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import IdentityAwareProxy, LoadBalancing
from diagrams.gcp.security import Iam
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Executive Strategy: Data Sovereignty", show=False, filename="strat_beyondcorp_access", direction="LR", graph_attr=graph_attr):
    exec_user = Tablet("Executive / Stakeholder")
    
    with Cluster("BeyondCorp Security Boundary"):
        lb = LoadBalancing("Global LB")
        iap = IdentityAwareProxy("IAP (Context Aware)")
        policy = Iam("Portfolio RBAC")

    command_hub = Rack("Executive Dashboard\n(Sensitive Financials)")

    exec_user >> lb >> iap
    iap >> Edge(label="Verify Identity", color="darkred") >> policy
    iap >> Edge(label="Need-to-Know Access", color="darkgreen") >> command_hub