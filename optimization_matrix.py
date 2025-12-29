from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

# Gold Standard attributes: Wide span, no white space
graph_attr = {
    "pad": "0.1",
    "nodesep": "2.0", 
    "ranksep": "2.5",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Carbon-Cost Optimization Matrix", show=False, filename="optimization_matrix", direction="LR", graph_attr=graph_attr):
    
    # Intelligence Layer representing the "Agent"
    optimizer = VertexAI("GreenOps AI Agent\n(Decision Engine)")

    with Cluster("Global Execution Regions"):
        high_perf = Run("Primary Region\n(High Carbon Intensity)")
        green_perf = Run("Carbon-Aware Region\n(Low Carbon / Scheduled)")

    # Horizontal Orchestration Logic
    optimizer >> Edge(label="Shift: Low Intensity Window", color="darkgreen", style="bold") >> green_perf
    optimizer >> Edge(label="Default: High Priority", color="darkblue", style="bold") >> high_perf