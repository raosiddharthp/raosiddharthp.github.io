from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Looker
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.database import Memorystore

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram("GreenOps Golden Signals", show=False, filename="golden_signals", direction="LR", graph_attr=graph_attr):
    
    metrics = Monitoring("Platform Health\n(Latency/Errors)")
    lake = BigQuery("Sustainability Lake\n(Carbon Metrics)")
    
    with Cluster("Observability Layer"):
        cache = Memorystore("Performance Cache")
        dashboard = Looker("ESG Compliance\n(Golden Signals)")

    # Flow
    metrics >> Edge(color="darkblue") >> cache
    lake >> Edge(color="darkgreen") >> cache
    cache >> Edge(label="Real-time Viz", style="bold") >> dashboard