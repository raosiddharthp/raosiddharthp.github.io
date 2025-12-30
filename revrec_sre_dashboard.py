from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Looker
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.database import Memorystore

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec SRE Dashboard", show=False, filename="revrec_sre_dashboard", direction="LR", graph_attr=graph_attr):
    telemetry = Monitoring("Golden Signals\n(L, T, E, S)")
    logs = BigQuery("Audit & SRE Logs")
    
    with Cluster("Visualization Engine"):
        cache = Memorystore("Metric Cache")
        dashboard = Looker("SRE Command Center")

    telemetry >> cache >> dashboard
    logs >> dashboard