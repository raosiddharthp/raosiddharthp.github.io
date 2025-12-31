from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack
from diagrams.generic.device import Tablet

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase D: LangGraph State Logic", 
    show=False, 
    filename="risk_langgraph_state", 
    direction="LR", 
    graph_attr=graph_attr
):
    entry = Rack("State Entry\n(Risk Event)")
    
    with Cluster("LangGraph Orchestration"):
        triage = VertexAI("Triage Agent")
        logic = Rack("Conditional Edge\n(Confidence Score)")
        
    closure = Rack("Auto-Close Case\n(Deterministic)")
    human = Tablet("Human-in-the-Loop\n(Escalation)")

    entry >> triage >> logic
    logic >> Edge(label="High Confidence", color="darkgreen") >> closure
    logic >> Edge(label="Low Confidence", color="darkred", style="bold") >> human