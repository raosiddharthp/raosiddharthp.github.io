from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run, Functions
from diagrams.gcp.storage import GCS
from diagrams.gcp.network import LoadBalancing

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Phase D: Technology Architecture", show=False, filename="doc_tech_architecture", direction="TB", graph_attr=graph_attr):
    ingress = LoadBalancing("API Gateway")
    
    with Cluster("Serverless Fabric (FinOps)"):
        trigger = Functions("Event Trigger")
        processor = Run("Cloud Run\n(Scalable Compute)")
        
    storage = GCS("Document Lake")

    ingress >> trigger >> processor >> storage