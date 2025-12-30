from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Risk Concentration Dendrogram", show=False, filename="contractguard_risk_dendrogram", direction="LR", graph_attr=graph_attr):
    source = BigQuery("Global Contract Fabric")
    
    with Cluster("Dendrogram Cluster Analysis (Hierarchical)"):
        processor = NaturalLanguageAPI("Clustering Logic")
        vendor_node = Tablet("Vendor Liability Hub")
        region_node = Tablet("Regional Risk Cluster")
        clause_node = Tablet("Indemnity Outliers")

    source >> processor >> [vendor_node, region_node, clause_node]