from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VPC
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.storage import GCS
from diagrams.gcp.security import SecurityScanner

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec VPC-SC Perimeter", show=False, filename="revrec_vpc_sc", direction="LR", graph_attr=graph_attr):
    external_bucket = GCS("External Unsafe Bucket")
    scanner = SecurityScanner("Audit / Monitoring")

    with Cluster("VPC Service Perimeter (Restricted)"):
        finance_vpc = VPC("Finance Data VPC")
        rev_lake = BigQuery("RevRec Dataset")
        contract_vault = GCS("Secure Contract Vault")

    external_bucket >> Edge(label="Blocked", color="red", style="bold") >> finance_vpc
    finance_vpc >> Edge(color="darkblue") >> [rev_lake, contract_vault]
    scanner - finance_vpc