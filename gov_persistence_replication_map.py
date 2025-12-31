from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.storage import GCS
from diagrams.generic.storage import Storage

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Operational: Persistence Map", 
    show=False, 
    filename="gov_persistence_replication_map", 
    direction="LR", 
    graph_attr=graph_attr
):
    with Cluster("Primary Region (Live)"):
        meta_p = BigQuery("Metadata (Sync)")
        raw_p = GCS("Raw Tier (Live)")

    with Cluster("DR Region (Backup)"):
        meta_s = BigQuery("Metadata (Replica)")
        raw_s = GCS("Raw Tier (Asynchronous)")

    meta_p >> Edge(label="Sync Replication", color="blue") >> meta_s
    raw_p >> Edge(label="Async Copy", color="gray", style="dashed") >> raw_s