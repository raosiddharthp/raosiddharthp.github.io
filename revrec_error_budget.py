from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Error Budget", show=False, filename="revrec_error_budget", direction="LR", graph_attr=graph_attr):
    lb = LoadBalancing("Global Traffic")
    
    with Cluster("Fiscal Freeze Window (100% Availability)"):
        active = Run("Stable Production Pods")
        policy = Monitoring("Error Budget Alert")

    lb >> active
    active >> Edge(label="Health Data") >> policy