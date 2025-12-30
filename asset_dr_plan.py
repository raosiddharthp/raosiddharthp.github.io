from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import Run
from diagrams.gcp.database import Spanner
from diagrams.gcp.storage import GCS

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "SRE View: Multi-Region DR", 
    show=False, 
    filename="asset_dr_plan", 
    direction="TB", 
    graph_attr=graph_attr
):
    lb = LoadBalancing("Global Load Balancer")

    with Cluster("Region: us-central1 (Primary)"):
        app_a = Run("Asset Service")
        db_a = Spanner("Global Database")

    with Cluster("Region: us-east4 (Secondary)"):
        app_b = Run("Asset Service")
        db_b = Spanner("Global Database")
        
    storage = GCS("Multi-Region Artifacts")

    lb >> [app_a, app_b]
    app_a >> db_a
    app_b >> db_b
    db_a >> Edge(label="Sync", style="dashed") >> db_b
    [app_a, app_b] >> storage