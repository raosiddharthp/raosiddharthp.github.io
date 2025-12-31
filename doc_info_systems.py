from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery, Dataflow

# TOGAF Phase C: Information Systems - Data Lineage
graph_attr = {
    "pad": "0.1", 
    "nodesep": "0.8", 
    "ranksep": "1.2", 
    "bgcolor": "transparent"
}

with Diagram(
    "Phase C: Information Systems", 
    show=False, 
    filename="doc_info_systems", 
    direction="LR", 
    graph_attr=graph_attr
):
    # Using VertexAI icon as a robust stand-in for Document AI
    doc_ai = VertexAI("Document AI\n(Extraction)")
    refinery = Dataflow("Schema Refinery\n(Normalization)")
    dw = BigQuery("BigQuery\n(Golden Records)")

    doc_ai >> Edge(label="Raw JSON") >> refinery >> Edge(label="Structured Data") >> dw