from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "MLOps: Artifact Lineage", 
    show=False, 
    filename="gov_artifact_lineage_receipt", 
    direction="LR", 
    graph_attr=graph_attr
):
    dataset = BigQuery("Training Dataset\n(Snapshot v1.2)")
    
    with Cluster("ML Metadata (Genealogy)"):
        params = Blank("Hyperparameters")
        execution = Rack("Training Execution")
        metrics = Blank("Accuracy/F1 Metrics")

    model = VertexAI("Final Model Artifact\n(Audit Verified)")

    dataset >> execution
    params >> execution
    execution >> metrics >> model