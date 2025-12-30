from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack
from diagrams.gcp.compute import Run
from diagrams.generic.device import Tablet

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "EA View: Multi-Agent Safety Guardrail", 
    show=False, 
    filename="asset_safety_guardrail", 
    direction="LR", 
    graph_attr=graph_attr
):
    primary_agent = VertexAI("Primary Planner Agent\n(Recommendation)")
    
    with Cluster("Safety Layer"):
        observer = VertexAI("Passive Observer\n(Safety Guardrail)")
        policy = Rack("Hard Safety Constraints\n(Lockout/Tagout)")

    action = Run("ERP Work-Order")
    block = Tablet("Safety Violation Block\n(Human Alert)")

    primary_agent >> observer
    observer >> Edge(label="Verify Policy") >> policy
    observer >> Edge(label="Safe", color="darkgreen") >> action
    observer >> Edge(label="Unsafe", color="red", style="bold") >> block