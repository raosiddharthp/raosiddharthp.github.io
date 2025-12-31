from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring
from diagrams.generic.network import Router

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase D: Global Failover Flow", 
    show=False, 
    filename="gov_global_failover_flow", 
    direction="TB", 
    graph_attr=graph_attr
):
    glb = LoadBalancing("Global Load Balancer")
    health = Monitoring("Regional Health Checks")

    with Cluster("Region: Europe (Primary)"):
        agent_eu = Run("Agent API EU")

    with Cluster("Region: Americas (Failover)"):
        agent_us = Run("Agent API US")

    glb >> Edge(label="Healthy", color="darkgreen") >> agent_eu
    glb >> Edge(label="Failover", color="darkred", style="dashed") >> agent_us
    health >> Edge(label="Probe", style="dotted") >> [agent_eu, agent_us]