from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Solution Context: Shared Service", show=False, filename="doc_safe_context", direction="LR", graph_attr=graph_attr):
    analyzer = Blank("Document Analyzer\n(Shared Service)")
    
    with Cluster("Business ARTs"):
        art_finance = Blank("Finance ART\n(RevRec)")
        art_legal = Blank("Legal ART\n(Contracts)")
        art_hr = Blank("HR ART\n(Onboarding)")

    analyzer >> Edge(color="blue", style="dashed") >> art_finance
    analyzer >> Edge(color="blue", style="dashed") >> art_legal
    analyzer >> Edge(color="blue", style="dashed") >> art_hr