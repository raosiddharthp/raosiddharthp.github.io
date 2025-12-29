from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Looker
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.database import Memorystore

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram("Executive Sustainability Dashboard", show=False, filename="executive_dashboard_arch", direction="LR", graph_attr=graph_attr):
    
    lake = BigQuery("Sustainability Lake\n(Aggregated ESG Data)")
    roai_engine = VertexAI("ROAI Calculation Engine\n(Cost vs Carbon)")

    with Cluster("Presentation Layer"):
        api_cache = Memorystore("Dashboard Cache")
        exec_ui = Looker("Executive Dashboard\n(Waterfall Charts)")

    # Data to Insight Flow
    lake >> Edge(label="Raw Metrics", color="darkblue") >> roai_engine
    roai_engine >> Edge(label="Financialized ESG", color="darkgreen") >> api_cache
    api_cache >> Edge(style="bold") >> exec_ui