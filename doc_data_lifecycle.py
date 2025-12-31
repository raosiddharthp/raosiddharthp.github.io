from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "bgcolor": "transparent"
}

with Diagram(
    "Data Architecture: Lifecycle", 
    show=False, 
    filename="doc_data_lifecycle", 
    direction="LR", 
    graph_attr=graph_attr
):
    source = GCS("Raw Uploads\n(Dark Data)")
    
    with Cluster("Processing Layer"):
        extractor = Run("Document AI\nProcessor")
        validator = Run("Schema Validator")
        
    warehouse = BigQuery("Golden Records\n(Structured)")
    viz = Rack("R Shiny Dashboard\n(Business Insights)")

    source >> extractor >> validator >> warehouse >> viz