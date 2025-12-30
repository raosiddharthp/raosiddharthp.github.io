from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.storage import GCS
from diagrams.generic.device import Tablet
from diagrams.gcp.database import Memorystore

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Value Stream: RCA Sequence", 
    show=False, 
    filename="asset_rca_sequence", 
    direction="LR", 
    graph_attr=graph_attr
):
    analyst = Tablet("Log Analyst Agent")
    
    with Cluster("Knowledge Fabric"):
        search = VertexAI("Vertex AI Search\n(RAG)")
        manuals = GCS("Technical Manuals\n(PDFs)")
        cache = Memorystore("Context Cache")

    analyst >> Edge(label="Query Context", color="darkblue") >> search
    search >> Edge(label="Retrieve Slabs") >> manuals
    search >> Edge(label="Return Insights") >> analyst
    analyst >> Edge(label="Update State") >> cache