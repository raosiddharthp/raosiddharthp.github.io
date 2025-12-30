from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VPC
from diagrams.gcp.compute import GCE
from diagrams.gcp.security import KeyManagementService

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Technology", show=False, filename="revrec_technology", direction="LR", graph_attr=graph_attr):
    tf = GCE("Terraform (IaC)")
    
    with Cluster("Multi-Region SOX Perimeter"):
        primary = VPC("Region: Primary")
        secondary = VPC("Region: Failover")
        kms = KeyManagementService("Audit Encryption")

    tf >> Edge(label="Immutable Deploy") >> [primary, secondary]
    [primary, secondary] - kms