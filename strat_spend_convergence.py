from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram(
    "Outcome: Spend Convergence", 
    show=False, 
    filename="strat_spend_convergence", 
    direction="LR", 
    graph_attr=graph_attr
):
    target = Rack("Planned Strategic Spend")
    
    with Cluster("Actuals Tracking"):
        actual = BigQuery("Operational Spend Data")
    
    convergence = Rack("Convergence Point\n(Strategy = Execution)")

    target >> Edge(color="blue") >> convergence
    actual >> Edge(color="darkgreen", style="dashed") >> convergence