from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Dataflow
from diagrams.gcp.storage import GCS
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase C: Automated Lineage", 
    show=False, 
    filename="gov_data_lineage_graph", 
    direction="LR", 
    graph_attr=graph_attr
):
    source = GCS("Raw Ingestion")
    
    with Cluster("Transformation & Quality Pipeline"):
        proc = Dataflow("Quality Validation")
        warehouse = BigQuery("Governance Lake")
        
    scorecard = Rack("Quality Scorecard\n(BCBS 239)")

    source >> proc >> warehouse >> scorecard