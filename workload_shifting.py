from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import GCE
from diagrams.gcp.operations import Monitoring

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Carbon-Aware Workload Shifting", show=False, filename="workload_shifting", direction="LR", graph_attr=graph_attr):
    
    traffic_in = LoadBalancing("Global HTTP(S)\nLoad Balancer")
    telemetry = Monitoring("Carbon Intensity\n(Live Signal)")

    with Cluster("Region A (High Intensity)"):
        node_a = GCE("Standard Cluster")

    with Cluster("Region B (Green Grid)"):
        node_b = GCE("Carbon-Optimized\nCluster")

    # Flow Logic
    telemetry >> Edge(label="Signal: Shift Required", color="darkred", style="dashed") >> traffic_in
    traffic_in >> Edge(label="Reroute", color="darkgreen", style="bold") >> node_b
    traffic_in >> Edge(label="Drain", color="gray", style="dotted") >> node_a