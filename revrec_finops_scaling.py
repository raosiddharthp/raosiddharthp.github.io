from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec FinOps Scaling", show=False, filename="revrec_finops_scaling", direction="LR", graph_attr=graph_attr):
    with Cluster("Standard Ops (Week 1-3)"):
        s2z = Run("Cloud Run\n(Scale-to-Zero)")
        bq_flex = BigQuery("BQ Flex Slots")

    with Cluster("10-Day Close Period"):
        dedicated = Run("Reserved Compute")
        bq_res = BigQuery("BQ Capacity\nReservations")

    scheduler = Monitoring("Fiscal Calendar\nTrigger")
    
    scheduler >> Edge(label="Close Start", color="orange") >> [dedicated, bq_res]