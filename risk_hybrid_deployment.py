from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase G: Hybrid MLE Deployment", show=False, filename="risk_hybrid_deployment", direction="TB", graph_attr=graph_attr):
    tf = Blank("Terraform\n(IaC Engine)")
    with Cluster("Bifurcated Model Plane"):
        with Cluster("Natural Language (NLP)"):
            bert = VertexAI("BERT Model\n(Text Triage)")
            text_api = Run("Text Endpoint")
        with Cluster("Structured Data (AutoML)"):
            bqml = BigQuery("BQML K-Means\n(Numeric Anomaly)")
            metric_api = Run("Numeric Endpoint")
    tf >> Edge(label="Deploy", style="dashed") >> [bert, bqml]
    [text_api, metric_api] >> Edge(label="Aggregated Score") >> Run("Risk Decision Hub")