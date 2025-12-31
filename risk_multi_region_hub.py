from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.compute import Run
from diagrams.generic.network import Router

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Tech View: Multi-Region Hub", 
    show=False, 
    filename="risk_multi_region_hub", 
    direction="LR", 
    graph_attr=graph_attr
):
    glb = LoadBalancing("Global Load Balancer")
    
    with Cluster("Region: us-central1 (Active)"):
        hub_a = Pubsub("Event Hub A")
        app_a = Run("Processor A")

    with Cluster("Region: us-east4 (Failover)"):
        hub_b = Pubsub("Event Hub B")
        app_b = Run("Processor B")

    external = Router("External Risk Feeds")

    external >> glb
    glb >> Edge(label="Healthy", color="darkgreen") >> hub_a
    glb >> Edge(label="Failover", color="darkred", style="dashed") >> hub_b
    hub_a >> app_a
    hub_b >> app_b