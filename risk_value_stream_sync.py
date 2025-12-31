from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack

# SAFe Strategic Alignment View
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "SAFe: Value Stream Sync", 
    show=False, 
    filename="risk_value_stream_sync", 
    direction="TB", 
    graph_attr=graph_attr
):
    with Cluster("Strategic Theme: Compliant Growth"):
        goal = Blank("Enterprise Risk Minimization")

    with Cluster("Enabling Value Stream"):
        risk_monitoring = Rack("Continuous Risk Monitoring")

    with Cluster("Operational Value Streams"):
        revrec = Rack("RevRec-AI")
        contract = Rack("ContractGuard")

    goal >> risk_monitoring
    risk_monitoring >> Edge(label="Enables Compliance", color="blue", style="dashed") >> [revrec, contract]