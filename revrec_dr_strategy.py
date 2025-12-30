from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import GCE
from diagrams.gcp.database import SQL

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec DR Strategy", show=False, filename="revrec_dr_strategy", direction="LR", graph_attr=graph_attr):
    lb = LoadBalancing("Global LB")

    with Cluster("Region: us-east1 (Active)"):
        app_a = GCE("RevRec App")
        db_a = SQL("Primary DB")

    with Cluster("Region: us-west1 (Active)"):
        app_b = GCE("RevRec App")
        db_b = SQL("Replica DB")

    lb >> Edge(color="darkblue") >> [app_a, app_b]
    app_a >> db_a
    app_b >> db_b
    db_a >> Edge(label="Sync Replication", color="red", style="bold") >> db_b