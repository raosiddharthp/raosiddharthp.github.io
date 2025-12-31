from diagrams import Diagram, Edge
from diagrams.gcp.analytics import Dataflow, BigQuery
from diagrams.generic.storage import Storage

graph_attr = {"pad": "0.1", "nodesep": "0.5", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase 1: Truth Layer", show=False, filename="gov_phase1_observability", direction="LR", graph_attr=graph_attr):
    source = Storage("Raw Data")
    ingest = Dataflow("Real-time Ingestion")
    dw = BigQuery("Truth Layer")
    
    source >> ingest >> dw