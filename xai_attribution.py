from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("XAI Feature Attribution View", show=False, filename="xai_attribution", direction="LR", graph_attr=graph_attr):
    
    agent_decision = VertexAI("GreenOps Agent\n(Decision Made)")

    with Cluster("Vertex Explainable AI (XAI)"):
        shaping = VertexAI("Feature Attribution\n(Shapley Values)")
        carbon_weight = VertexAI("Carbon Weight: 75%")
        cost_weight = VertexAI("Cost Weight: 25%")

    auditor_report = Run("Audit-Ready\nExplanation PDF")

    # Trace Flow
    agent_decision >> Edge(label="Explain Request", color="darkblue") >> shaping
    shaping >> carbon_weight
    shaping >> cost_weight
    [carbon_weight, cost_weight] >> Edge(label="Synthesize", color="darkgreen") >> auditor_report