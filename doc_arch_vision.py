from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank
from diagrams.gcp.analytics import Dataprep

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase A: Architecture Vision", show=False, filename="doc_arch_vision", direction="LR", graph_attr=graph_attr):
    chaos = Blank("Dark Data Chaos\n(Unstructured)")
    vision = Dataprep("Target State:\nZero-Latency Service")
    portfolio = Blank("Portfolio Foundation\n(Clean Ingestion)")

    chaos >> Edge(label="Digital Transformation", color="darkred") >> vision >> Edge(color="darkblue", style="bold") >> portfolio