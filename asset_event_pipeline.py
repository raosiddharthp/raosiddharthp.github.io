from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow, BigQuery
from diagrams.gcp.iot import IotCore
from diagrams.generic.device import Tablet

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase D: Event-Driven Pipeline", 
    show=False, 
    filename="asset_event_pipeline", 
    direction="LR", 
    graph_attr=graph_attr
):
    gateways = Tablet("IoT Gateways\n(Field Assets)")
    
    with Cluster("Ingestion & Processing"):
        ingress = IotCore("IoT Core")
        bus = Pubsub("Telemetry Bus")
        stream = Dataflow("Streaming ETL")
        
    warehouse = BigQuery("Reliability Lake")

    gateways >> ingress >> bus >> stream >> warehouse