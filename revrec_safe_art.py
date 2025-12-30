from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Change Management", show=False, filename="revrec_safe_art", direction="LR", graph_attr=graph_attr):
    cfo = Run("CFO Steering\nCommittee")
    
    with Cluster("Agile Release Train (ART)"):
        product = Run("Product Management")
        dev_teams = [Run("AI Team"), Run("ERP Team"), Run("Audit Team")]

    feedback = Run("Continuous Alignment")

    cfo >> Edge(label="Strategic Guardrails") >> product
    product >> dev_teams
    dev_teams >> Edge(style="dashed") >> feedback >> cfo