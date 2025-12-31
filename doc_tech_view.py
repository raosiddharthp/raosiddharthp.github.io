from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.gcp.security import Iam, IAP
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Technology Lens: SecOps", show=False, filename="doc_tech_view", direction="LR", graph_attr=graph_attr):
    gatekeeper = IAP("IAP Access")
    with Cluster("VPC Service Perimeter"):
        vpc = VirtualPrivateCloud("Secure Network")
        model = VertexAI("Private HF Endpoint")
    gatekeeper >> Edge(label="Authorize") >> vpc >> model