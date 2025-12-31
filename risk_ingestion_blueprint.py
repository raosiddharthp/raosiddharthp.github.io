from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow, BigQuery
from diagrams.gcp.compute import Run
from diagrams.generic.network import Firewall

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Cloud Arch: High-Throughput Ingestion", 
    show=False, 
    filename="risk_ingestion_blueprint", 
    direction="LR", 
    graph_attr=graph_attr
):
    events = Firewall("Millions of Events\n(L7 Ingress)")
    
    with Cluster("Ingestion Backbone (99.9% SLA)"):
        bus = Pubsub("Real-Time Event Bus")
        stream = Dataflow("Stream Processor\n(Sanitization)")
        
    storage = BigQuery("Strategic Risk Lake")
    swarm = Run("Agent Swarm Trigger")

    events >> bus >> stream
    stream >> storage
    stream >> Edge(label="Notify") >> swarm