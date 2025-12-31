from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.security import Iam, KeyManagementService
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.network import VirtualPrivateCloud

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Phase G: Implementation Governance", show=False, filename="doc_imp_governance", direction="LR", graph_attr=graph_attr):
    with Cluster("Sovereign Security Perimeter"):
        vpc_sc = VirtualPrivateCloud("VPC-SC Perimeter")
        kms = KeyManagementService("Encryption")
        
    loop = VertexAI("Continuous Training Loop\n(Model Drift)")

    vpc_sc >> Edge(label="Protect") >> loop