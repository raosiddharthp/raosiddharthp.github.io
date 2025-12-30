from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.devtools import GCR
from diagrams.onprem.vcs import Github

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Technical Lineage", show=False, filename="revrec_technical_lineage", direction="LR", graph_attr=graph_attr):
    journal_entry = BigQuery("General Ledger\nEntry")
    
    with Cluster("Traceability Metadata"):
        dataset = BigQuery("Dataset Version\n(Snapshot ID)")
        code = Github("Code Commit\n(SHA-1)")
        lineage = DataCatalog("Lineage Graph")

    journal_entry >> Edge(color="purple", style="dotted") >> lineage
    lineage >> [dataset, code]