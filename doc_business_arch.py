from diagrams import Diagram, Cluster, Edge
from diagrams.generic.device import Tablet
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.6", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase B: Business Architecture", show=False, filename="doc_business_arch", direction="LR", graph_attr=graph_attr):
    with Cluster("Value Stream: Inquiry-to-Resolution"):
        inquiry = Tablet("Customer Inquiry")
        triage = Rack("Manual Triage\n(Friction Point)")
        resolution = Tablet("Resolved Action")

    inquiry >> Edge(label="Document Upload") >> triage >> resolution