from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.compute import Functions
from diagrams.gcp.security import Iam
from diagrams.gcp.operations import Logging

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase D: Resilience & Self-Healing", 
    show=False, 
    filename="risk_resilience_landing_zone", 
    direction="TB", 
    graph_attr=graph_attr
):
    glb = LoadBalancing("Global Load Balancer")
    
    with Cluster("Region: Multi-Site Ingestion"):
        feed = Pubsub("Risk Event Stream\n(Snapshots Enabled)")
        
    with Cluster("Self-Healing Cycle"):
        trigger = Functions("Quarantine Trigger\n(Cloud Function)")
        policy = Iam("Dynamic IAM Policy\n(Account Lockdown)")
        audit = Logging("Audit Logs\n(Chain of Custody)")

    glb >> feed
    feed >> Edge(label="Detect Suspect") >> trigger
    trigger >> policy
    trigger >> audit