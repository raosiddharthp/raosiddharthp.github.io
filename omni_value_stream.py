from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase B: Business Value Stream", show=False, filename="omni_value_stream", direction="LR", graph_attr=graph_attr):
    start = Blank("Call Inception\n(Customer Need)")
    
    with Cluster("Legacy Path (High Friction)"):
        ivr = Blank("Static IVR\n(Wait Time)")
        agent = Blank("Manual Triage\n($$$)")
        
    with Cluster("OmniMind Path (Optimized)"):
        ai = Blank("Agentic Flash\n(Sub-Second)")
        resolved = Blank("Autonomous\nResolution")

    start >> Edge(color="red", label="Waste") >> ivr >> agent >> Blank("Resolution")
    start >> Edge(color="darkgreen", style="bold") >> ai >> resolved