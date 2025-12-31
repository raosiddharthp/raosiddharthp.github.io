from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase H: Drift Retraining Loop", 
    show=False, 
    filename="gov_drift_retraining_loop", 
    direction="LR", 
    graph_attr=graph_attr
):
    prod_model = VertexAI("Production Model\n(Live Inference)")
    monitor = Monitoring("Vertex AI Model Monitoring\n(Threshold Check)")
    
    with Cluster("Automated Retraining Job"):
        pipeline = VertexAI("Vertex AI Pipelines")
        evaluator = VertexAI("Model Evaluation")
        registry = Rack("Model Registry")

    prod_model >> monitor
    monitor >> Edge(label="Drift Detected", color="red") >> pipeline
    pipeline >> evaluator >> registry >> Edge(label="Hot Swap", style="dashed") >> prod_model