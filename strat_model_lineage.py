from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.storage import GCS
from diagrams.gcp.devtools import GCR

# TOGAF Phase G: Implementation Governance
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase G: Model Lineage", 
    show=False, 
    filename="strat_model_lineage", 
    direction="LR", 
    graph_attr=graph_attr
):
    source_data = BigQuery("Strategic Data Lake\n(OKR/Fin)")
    
    with Cluster("MLOps Pipeline"):
        training = VertexAI("AutoML / Training")
        artifact = GCS("Model Artifacts\n(Versioned)")
        registry = GCR("Model Registry")

    endpoint = VertexAI("Production Endpoint\n(Live Inference)")

    source_data >> training >> artifact >> registry >> endpoint