from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.security import Iam
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.generic.network import Firewall
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("TOGAF Artifact: Risk Heat Map", show=False, filename="risk_governance_heatmap", direction="LR", graph_attr=graph_attr):
    initial_risk = Rack("Initial Risk\n(Unfiltered Traffic)")
    with Cluster("Security Mitigation (GCP)"):
        armor = Firewall("Cloud Armor\n(L7 Filter)")
        vpc_sc = VirtualPrivateCloud("VPC-SC Perimeter")
        iam = Iam("Identity-Aware Access")
    residual_risk = Rack("Residual Risk\n(Mitigated & Audited)")
    initial_risk >> Edge(label="Mitigate", color="darkred") >> armor >> vpc_sc >> iam >> Edge(color="darkgreen", style="bold") >> residual_risk