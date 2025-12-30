from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Vision & Business", show=False, filename="revrec_vision_biz", direction="LR", graph_attr=graph_attr):
    contract = Run("Contract Management")
    biz_cap = VertexAI("Capability:\nAI-Driven RevRec")
    leakage_reduction = Run("Benefit:\nZero-Leakage Recognition")

    contract >> Edge(label="Strategic Alignment", color="darkblue") >> biz_cap >> Edge(label="Outcome", color="darkgreen") >> leakage_reduction