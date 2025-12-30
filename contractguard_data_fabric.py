from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.database import Firestore, Memorystore
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase C: Semantic Data Fabric", show=False, filename="contractguard_data_fabric", direction="LR", graph_attr=graph_attr):
    raw_docs = GCS("Contract Vault (PDFs)")
    
    with Cluster("Semantic Processing Layer"):
        rag_engine = VertexAI("RAG Orchestrator")
        vector_db = Memorystore("FAISS Vector DB")
        metadata = Firestore("Firestore Metadata")

    warehouse = BigQuery("Risk & Analytics Fabric")

    raw_docs >> rag_engine
    rag_engine >> [vector_db, metadata]
    metadata >> warehouse