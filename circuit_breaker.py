from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.devtools import GCR

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram("Sustainability Circuit Breaker", show=False, filename="circuit_breaker", direction="LR", graph_attr=graph_attr):
    
    detector = Monitoring("Carbon Drift Detector\n(Threshold Monitor)")
    
    with Cluster("Active Agent Environment"):
        agent = VertexAI("Operational Agent\n(GreenOps Pilot)")
        status = GCR("Kill Switch / State")

    alert = Monitoring("Audit Alert\n(Quality Degradation)")

    # Logical Flow
    detector >> Edge(label="Drift > 15%", color="darkred", style="bold") >> status
    status >> Edge(label="Suspend", color="red") >> agent
    alert >> Edge(label="Trigger Audit", color="orange") >> status