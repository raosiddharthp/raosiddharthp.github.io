from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, BigQuery
from diagrams.gcp.storage import GCS
from diagrams.gcp.database import Memorystore
from diagrams.gcp.ml import NaturalLanguageAPI

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "TOGAF Phase C: Data Ingestion Flow", 
    show=False, 
    filename="asset_ingestion_flow", 
    direction="LR", 
    graph_attr=graph_attr
):
    with Cluster("Structured Stream"):
        telemetry = Pubsub("IoT Telemetry")
        warehouse = BigQuery("Structured Data Lake")

    with Cluster("Unstructured Stream"):
        logs = GCS("Raw Logs/Manuals")
        vector_db = Memorystore("Vector Search\n(FAISS Index)")
        embed = NaturalLanguageAPI("Embeddings Engine")

    telemetry >> warehouse
    logs >> embed >> vector_db