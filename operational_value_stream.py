from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram("Operational Value Stream Map", show=False, filename="operational_value_stream", direction="LR", graph_attr=graph_attr):
    
    ingest = Pubsub("Telemetry Ingestion")
    
    with Cluster("Manual Bottlenecks (Legacy)"):
        manual_analysis = Run("Manual Data Audit\n(2-3 Days)")
        manual_approval = Run("Ops Approval\n(1 Day)")

    with Cluster("Agentic Optimization (Target)"):
        agent_logic = VertexAI("GreenOps Pilot\n(Sub-Second)")
        auto_shift = Run("Automated Region Shift")

    # Flow
    ingest >> Edge(label="Legacy Path", color="red", style="dashed") >> manual_analysis >> manual_approval
    ingest >> Edge(label="AI Path", color="darkgreen", style="bold") >> agent_logic >> auto_shift