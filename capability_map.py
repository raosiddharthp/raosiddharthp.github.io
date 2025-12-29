from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import GCE
from diagrams.gcp.network import CDN
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Sustainability Capability Map", show=False, filename="capability_map", direction="LR", graph_attr=graph_attr):
    with Cluster("Resource Optimization"):
        res = GCE("Carbon-Aware Rightsizing")
        mon = Monitoring("Real-time Utilization")
    
    with Cluster("Regional Strategy"):
        reg = CDN("Regional Shifting")
        grid = Monitoring("Grid Intensity Tracking")

    res >> Edge(color="darkgreen", label="Optimized Flow") >> reg