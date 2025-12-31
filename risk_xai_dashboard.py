from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import Looker
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "EA View: Feature Attribution (XAI)", 
    show=False, 
    filename="risk_xai_dashboard", 
    direction="LR", 
    graph_attr=graph_attr
):
    model = VertexAI("Predictive Model\n(Risk Scorer)")
    
    with Cluster("Explainability Engine"):
        attribution = VertexAI("Vertex Explainable AI\n(SHAP/IG Weights)")
        logic = Rack("Feature Mapping\n(Freq/Amt/Loc)")

    audit_view = Looker("XAI Audit Dashboard")

    model >> attribution >> logic >> audit_view