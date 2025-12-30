from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Agentic ROI Waterfall", show=False, filename="contractguard_roi_waterfall", direction="LR", graph_attr=graph_attr):
    with Cluster("Cost & Investment"):
        tco = Monitoring("Agentic TCO\n(GCP Infra + Dev)")
    
    with Cluster("Value Realized"):
        labor = Rack("Manual Labor Offset")
        risk = Rack("Risk Mitigation Value")

    net_value = Rack("Net Positive ROI")

    tco >> Edge(color="red") >> labor >> Edge(color="darkgreen") >> risk >> Edge(color="darkblue", style="bold") >> net_value