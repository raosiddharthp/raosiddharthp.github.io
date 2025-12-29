from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, BigQuery, Dataflow
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.database import Memorystore

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram("Information Systems Architecture", show=False, filename="info_systems_arch", direction="LR", graph_attr=graph_attr):
    
    ingest = Pubsub("Streaming\nTelemetry")
    
    with Cluster("Intelligence Warehouse"):
        processing = Dataflow("ETL / Normalization")
        warehouse = BigQuery("Sustainability Lake")
        vector_store = Memorystore("Vector Embeddings\n(RAG Layer)")

    agent_layer = VertexAI("Agentic Reasoning\n(Contextual Retrieval)")

    # Flow
    ingest >> processing >> warehouse
    warehouse >> Edge(label="Indexing", color="darkblue") >> vector_store
    vector_store >> Edge(label="Augmented Context", color="darkgreen", style="bold") >> agent_layer