from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Phase A: Capability Value Map", show=False, filename="omni_capability_value_map", direction="LR", graph_attr=graph_attr):
    with Cluster("AI Capabilities"):
        intent = Blank("Intent Recognition")
        sentiment = Blank("Sentiment Analysis")
        rag = Blank("Agentic RAG")
        
    with Cluster("Strategic KPIs"):
        csat = Blank("↑ CSAT Score")
        aht = Blank("↓ Avg Handle Time")
        fcr = Blank("↑ First Call Resolution")

    intent >> csat
    sentiment >> aht
    rag >> fcr