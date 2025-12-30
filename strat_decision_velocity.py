from diagrams import Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram(
    "Outcome: Decision Velocity J-Curve", 
    show=False, 
    filename="strat_decision_velocity", 
    direction="LR", 
    graph_attr=graph_attr
):
    manual = Rack("Manual Aggregation\n(Linear/Slow)")
    pivot = Run("Executive Dashboard\n(The Pivot Point)")
    automated = Rack("Strategic Synthesis\n(Exponential Velocity)")

    manual >> Edge(label="Transformation", color="orange") >> pivot >> Edge(label="Scale Realized", color="darkgreen", style="bold") >> automated