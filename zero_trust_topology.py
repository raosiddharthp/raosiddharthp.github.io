from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VPC
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI

# Robust imports for Security components
try:
    from diagrams.gcp.security import Iap as IAP, Armor as CloudArmor
except ImportError:
    try:
        from diagrams.gcp.security import IdentityAwareProxy as IAP, CloudArmor
    except ImportError:
        # Fallback to generic icons if specific ones are missing
        from diagrams.gcp.security import SecurityScanner as IAP, SecurityScanner as CloudArmor

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Zero-Trust Perimeter Topology", show=False, filename="zero_trust_topology", direction="LR", graph_attr=graph_attr):
    
    user = IAP("Identity-Aware\nProxy")
    shield = CloudArmor("Cloud Armor\n(WAF/DDoS)")

    with Cluster("Sovereign Data Perimeter (VPC-SC)"):
        vpc_net = VPC("ESG Data VPC")
        data_fabric = BigQuery("Sustainability Lake")
        ai_engine = VertexAI("GreenOps AI")

    # Security Flow
    user >> Edge(label="Authorized Access", color="darkgreen") >> vpc_net
    shield >> Edge(label="Packet Inspection") >> vpc_net
    vpc_net >> [data_fabric, ai_engine]