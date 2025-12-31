from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.gcp.security import IAP, KeyManagementService
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase D: Network Topology", show=False, filename="omni_network_topology", direction="TB", graph_attr=graph_attr):
    iap = IAP("IAP Gatekeeper")
    
    with Cluster("VPC Service Perimeter (VPC-SC)"):
        with Cluster("Compute Tier"):
            swarm = Run("Agentic Swarm\n(Cloud Run)")
        
        with Cluster("AI Tier"):
            brain = VertexAI("Gemini 1.5\nEndpoint")
            kms = KeyManagementService("Cloud KMS")
            
        vpc = VirtualPrivateCloud("Shared VPC")

    iap >> vpc >> swarm >> brain
    kms >> Edge(style="dotted") >> brain