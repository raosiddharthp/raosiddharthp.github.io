from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Tablet
from diagrams.gcp.devtools import GCR

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase H: Model Governance Framework", 
    show=False, 
    filename="asset_model_governance", 
    direction="LR", 
    graph_attr=graph_attr
):
    drift = Monitoring("Drift Detected\n(Model Performance)")
    
    with Cluster("Governance & Audit"):
        hitl = Tablet("HITL Review\n(Subject Matter Expert)")
        audit_log = VertexAI("Audit Trace\n(Governance Log)")
        
    registry = GCR("Model Registry\n(Staging -> Prod)")
    deploy = VertexAI("Automated Deployment")

    drift >> Edge(label="Alert", color="red") >> hitl
    hitl >> Edge(label="Approve", color="darkgreen") >> registry
    hitl >> audit_log
    registry >> deploy