from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.generic.database import SQL
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Current State", show=False, filename="revrec_current_state", direction="LR", graph_attr=graph_attr):
    crm = GCS("CRM / Contract Data\n(Unstructured)")
    
    with Cluster("Manual Processing Zone"):
        spreadsheet = Run("Manual Excel\nTransfers")
        judgment = Run("Human Review\n(Audit Bottleneck)")

    erp = SQL("Legacy ERP\n(General Ledger)")

    crm >> Edge(label="Manual Export", color="red") >> spreadsheet >> judgment >> Edge(label="Manual Entry") >> erp