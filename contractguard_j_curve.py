from diagrams import Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Approval Velocity J-Curve", show=False, filename="contractguard_j_curve", direction="LR", graph_attr=graph_attr):
    manual = Run("Legacy Process\n(Linear/Bottlenecked)")
    pivot = Rack("ContractGuard Implementation\n(The Pivot Point)")
    automated = Run("AI-Augmented Velocity\n(Exponential Growth)")

    manual >> Edge(label="Digital Transformation", color="darkorange") >> pivot >> Edge(label="Scale Realized", color="darkgreen", style="bold") >> automated