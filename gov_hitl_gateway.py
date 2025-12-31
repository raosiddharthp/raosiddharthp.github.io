from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.generic.device import Tablet
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Governance: HITL Gateway", 
    show=False, 
    filename="gov_hitl_gateway", 
    direction="LR", 
    graph_attr=graph_attr
):
    system = Run("AI Validation Swarm")
    
    with Cluster("HITL Threshold Gate"):
        logic = Rack("Rule: Is Financial\nHigh-Risk?")
        human = Tablet("Governance Council\n(Sign-off)")

    commit = Rack("Finalized Metadata")

    system >> logic
    logic >> Edge(label="High Risk", color="red") >> human
    human >> commit
    logic >> Edge(label="Low Risk", color="green", style="dashed") >> commit