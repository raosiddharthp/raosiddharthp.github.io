from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "TOGAF Phase D: Agent State Machine", 
    show=False, 
    filename="asset_agent_state_machine", 
    direction="LR", 
    graph_attr=graph_attr
):
    trigger = Pubsub("Telemetry Trigger\n(Pub/Sub)")
    
    with Cluster("LangGraph Orchestration"):
        monitor = VertexAI("Monitor Agent\n(Anomaly Detection)")
        diagnose = VertexAI("Diagnostic Agent\n(RCA)")
        planner = VertexAI("Planner Agent\n(Work Order)")

    handoff = Run("Maintenance Handoff\n(ServiceNow)")

    trigger >> monitor >> Edge(label="Anomaly Found") >> diagnose >> Edge(label="Context Ready") >> planner >> handoff