from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring, Logging
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("SRE: CCAI Health Dashboard", show=False, filename="omni_health_dashboard", direction="LR", graph_attr=graph_attr):
    telemetry = [Monitoring("Metrics"), Logging("Logs")]
    warehouse = BigQuery("Ops Data Warehouse")
    looker = Rack("Looker Dashboard\n(CSAT/Token ROI)")

    telemetry >> warehouse >> looker