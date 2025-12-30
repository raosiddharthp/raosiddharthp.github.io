from diagrams import Diagram, Edge
from diagrams.gcp.analytics import BigQuery, Looker

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Data Arch: BigQuery Analytics", show=False, filename="contractguard_bigquery_analytics", direction="LR", graph_attr=graph_attr):
    warehouse = BigQuery("BigQuery\n(Risk Heatmap Data)")
    viz = Looker("Looker\n(Global Trends)")
    
    warehouse >> Edge(label="Analyze", color="purple") >> viz