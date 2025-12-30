from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec SAFe Delivery", show=False, filename="revrec_safe_delivery", direction="LR", graph_attr=graph_attr):
    pi_plan = Run("PI Planning")
    
    with Cluster("Agile Release Train (ART)"):
        sprint1 = Run("Iteration 1")
        sprint2 = Run("Iteration 2")
        demo = Run("System Demo")

    pi_plan >> sprint1 >> sprint2 >> demo