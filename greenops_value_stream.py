from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import Pubsub, BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.iot import IotCore

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("ESG Value Stream", show=False, filename="greenops_value_stream", direction="LR", graph_attr=graph_attr):

    telemetry = IotCore("Carbon Telemetry\n(Ingestion)")
    stream = Pubsub("Real-time\nData Stream")
    
    with Cluster("Processing & Intelligence"):
        warehouse = BigQuery("Carbon Data Lake")
        # Industry standard: Using VertexAI for the synthesis logic
        narrative_gen = VertexAI("Gemini 1.5 Pro\n(Narrative Engine)")

    report = Run("Automated ESG\nReport (PDF/XBRL)")

    # Flow
    telemetry >> Edge(label="Raw Data", color="darkgreen") >> stream >> warehouse
    warehouse >> Edge(label="Contextual Insights", color="darkgreen") >> narrative_gen
    narrative_gen >> Edge(label="Drafting", color="darkgreen", style="bold") >> report