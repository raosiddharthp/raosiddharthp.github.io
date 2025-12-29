from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.devtools import GCR
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("MLOps CI/CD/CT Lifecycle", show=False, filename="mlops_lifecycle", direction="LR", graph_attr=graph_attr):
    
    # Using GCR as the build/trigger icon to avoid the CloudBuild ImportError
    git_trigger = GCR("CI/CD Trigger\n(Git Push)")
    
    with Cluster("Continuous Training (CT) Pipeline"):
        data_source = BigQuery("Training Data")
        trainer = VertexAI("Vertex AI Training\n(Auto-Retrain)")
        evaluator = VertexAI("Model Evaluation")

    registry = GCR("Model Registry\n(Versioned)")
    endpoint = VertexAI("Production\nPrediction API")

    # Pipeline Flow
    git_trigger >> Edge(label="Build/Test", color="darkblue") >> trainer
    data_source >> trainer >> evaluator
    evaluator >> Edge(label="Push if Acc > Threshold", color="darkgreen") >> registry
    registry >> Edge(label="CD Deployment", style="bold") >> endpoint