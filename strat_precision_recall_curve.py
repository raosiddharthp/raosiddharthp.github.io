from diagrams import Diagram, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Statistical Performance: Precision-Recall", 
    show=False, 
    filename="strat_precision_recall_curve", 
    direction="LR", 
    graph_attr=graph_attr
):
    recall = Monitoring("Recall\n(High-Risk Capture)")
    precision = Monitoring("Precision\n(False Positive Rate)")
    
    tradeoff = Rack("Strategic Threshold\n(Prioritizing Recall)")

    [recall, precision] >> tradeoff