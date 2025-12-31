from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.gcp.security import KeyManagementService, Iam
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase D: VPC-SC Security Fortress", 
    show=False, 
    filename="risk_vpcsc_fortress", 
    direction="TB", 
    graph_attr=graph_attr
):
    iam = Iam("Access Policy\n(Identity)")

    with Cluster("VPC Service Perimeter"):
        with Cluster("Protected Data Plane"):
            warehouse = BigQuery("Risk Logic (BQML)")
            swarm = Run("Agent Swarm")
        
        vpc = VirtualPrivateCloud("VPC Security Perimeter")
        kms = KeyManagementService("Encryption at Rest")

    iam >> vpc
    vpc >> Edge(label="Authorize") >> warehouse
    warehouse >> swarm
    kms >> Edge(label="Guard", style="dotted") >> warehouse