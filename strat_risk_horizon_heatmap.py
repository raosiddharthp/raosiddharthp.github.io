from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Looker
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

# TOGAF Phase H: Architecture Change Management
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase H: Risk Horizon Heatmap", 
    show=False, 
    filename="strat_risk_horizon_heatmap", 
    direction="LR", 
    graph_attr=graph_attr
):
    auditor = VertexAI("Auditor Agent\n(Risk Predictor)")
    
    with Cluster("Risk Horizon Mapping"):
        pre_impl = Rack("Pre-Implementation\n(High Latency Risk)")
        post_impl = Rack("Post-Implementation\n(Real-Time Visibility)")

    heatmap = Looker("Portfolio Risk Heatmap")

    auditor >> Edge(label="Predictive Audit", color="darkred") >> pre_impl
    auditor >> Edge(label="Gap Mitigation", color="darkgreen", style="bold") >> post_impl
    [pre_impl, post_impl] >> heatmap