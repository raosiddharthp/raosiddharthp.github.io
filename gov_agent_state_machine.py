from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Logging
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase D: Agentic State Logic", 
    show=False, 
    filename="gov_agent_state_machine", 
    direction="LR", 
    graph_attr=graph_attr
):
    entry = Rack("Data Ingress")
    
    with Cluster("LangGraph Swarm"):
        profiler = VertexAI("Profiling Agent")
        critic = VertexAI("Quality Critic")
        supervisor = VertexAI("Council Supervisor")
        
    audit = Logging("Transparent Log\n(Chain of Thought)")
    storage = Rack("Validated Truth Layer")

    entry >> profiler >> critic >> supervisor
    supervisor >> Edge(label="Log Path") >> audit
    supervisor >> Edge(label="Commit") >> storage