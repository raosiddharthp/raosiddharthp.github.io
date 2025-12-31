from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Document Intelligence Value Stream", show=False, filename="doc_value_stream_map", direction="LR", graph_attr=graph_attr):
    raw = Blank("Raw Unstructured\nDocument")
    extraction = Blank("Automated\nExtraction")
    context = Blank("Agentic\nContextualization")
    action = Blank("Business\nAction/Decision")

    raw >> Edge(color="blue") >> extraction >> Edge(color="blue") >> context >> Edge(color="darkgreen", style="bold") >> action