from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
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
    "SRE: Intelligence Feedback Loop", 
    show=False, 
    filename="gov_intelligence_loop", 
    direction="LR", 
    graph_attr=graph_attr
):
    detect = VertexAI("Drift Detection\n(Monitoring)")
    
    with Cluster("Automated Remediation"):
        swarm = Run("Agent Swarm")
        proposal = Rack("Suggested Validation Rules")

    steward = Tablet("Data Steward\n(Approval)")

    detect >> Edge(label="Signal") >> swarm >> proposal >> steward
    steward >> Edge(label="Deploy Rule", style="dashed") >> detect