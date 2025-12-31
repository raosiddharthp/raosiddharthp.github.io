from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.devtools import Build, GCR
from diagrams.gcp.compute import Functions
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "0.8",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "MLOps: Vertex AI Pipeline", 
    show=False, 
    filename="doc_mlops_pipeline", 
    direction="LR", 
    graph_attr=graph_attr
):
    drift_trigger = Rack("Drift Detected\n(Threshold Check)")
    
    with Cluster("Vertex AI Orchestration"):
        cicd = Build("Cloud Build\n(Unit Tests)")
        registry = GCR("Model Registry")
        train = VertexAI("Automated Training\n(CT)")
        
    deploy = Functions("Agent Update\n(Hot Swap)")

    drift_trigger >> cicd >> registry >> train >> deploy