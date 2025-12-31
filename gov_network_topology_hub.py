from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.generic.network import Router, Switch

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Phase D: Secure Hub-and-Spoke", show=False, filename="gov_network_topology_hub", direction="TB", graph_attr=graph_attr):
    with Cluster("VPC Service Perimeter (VPC-SC)"):
        with Cluster("Hub Project (Common Services)"):
            hub_vpc = VirtualPrivateCloud("Shared VPC Hub")
            fw = Router("Central Firewall")
        with Cluster("Spoke A (Ingestion)"):
            ingest_vpc = VirtualPrivateCloud("Ingestion VPC")
        with Cluster("Spoke B (AI/ML Logic)"):
            ai_vpc = VirtualPrivateCloud("Governance AI VPC")
    peer1 = Switch("VPC Peering A")
    peer2 = Switch("VPC Peering B")
    hub_vpc >> Edge(color="blue") >> peer1 >> ingest_vpc
    hub_vpc >> Edge(color="blue") >> peer2 >> ai_vpc