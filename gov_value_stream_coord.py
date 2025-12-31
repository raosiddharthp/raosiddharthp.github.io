from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.2", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("SAFe: Value Stream Enablers", show=False, filename="gov_value_stream_coord", direction="TB", graph_attr=graph_attr):
    with Cluster("Strategic Intent"):
        goal = Blank("Data Trust")

    with Cluster("Enabling Value Stream (Data Quality)"):
        p1 = Blank("P1: Ingestion")
        p2 = Blank("P2: ML Tagging")
        p3 = Blank("P3: Agentic Validation")

    goal >> p1 >> p2 >> p3