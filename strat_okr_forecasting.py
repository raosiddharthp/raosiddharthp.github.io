from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Pubsub
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Executive Strategy: Predictive OKRs", show=False, filename="strat_okr_forecasting", direction="LR", graph_attr=graph_attr):
    data_lake = BigQuery("Historical OKR Data")
    
    with Cluster("Prophet Analytics Engine (R)"):
        compute = Run("Time-Series Forecast")
        logic = Rack("Forecasting Model\n(Seasonality/Trend)")

    alert_bus = Pubsub("Target Miss Thresholds")
    exec_view = Rack("Executive Dashboard")

    data_lake >> compute >> logic >> alert_bus >> exec_view