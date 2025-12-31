from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run, Functions
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.gcp.security import IAP, KeyManagementService
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.2", "nodesep": "1.2", "ranksep": "1.8", "bgcolor": "transparent"}

with Diagram("Zero-Trust Serverless Blueprint", show=False, filename="doc_zero_trust_blueprint", direction="TB", graph_attr=graph_attr):
    user = IAP("IAP Gatekeeper")
    with Cluster("VPC-SC Perimeter"):
        with Cluster("Compute Spoke"):
            app = Run("Analyzer Engine")
            trigger = Functions("Event Handler")
        with Cluster("AI Spoke"):
            model = VertexAI("Llama/Gemini API")
            kms = KeyManagementService("Cloud KMS")
        network = VirtualPrivateCloud("Shared VPC")
    user >> network >> app
    app >> trigger
    app >> Edge(label="Encrypted") >> model
    kms >> Edge(style="dotted") >> model