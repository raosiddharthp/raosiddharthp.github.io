from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.devtools import GCR

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Vertex Pipeline", show=False, filename="revrec_vertex_pipeline", direction="LR", graph_attr=graph_attr):
    data = BigQuery("Training Data\n(IFRS 15 Labelling)")

    with Cluster("Vertex AI Pipeline"):
        train = VertexAI("Training")
        eval = VertexAI("Evaluation")
        reg = GCR("Model Registry")

    deploy = VertexAI("Endpoint Deployment")

    data >> train >> eval >> reg >> deploy