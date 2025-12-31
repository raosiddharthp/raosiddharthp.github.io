from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Phase B: ROI Model Waterfall", show=False, filename="omni_roi_model", direction="TB", graph_attr=graph_attr):
    current_cost = Rack("Baseline OpEx\n($10M/yr)")
    
    with Cluster("Savings Levers"):
        deflection = Blank("80% Deflection\n(-$4M)")
        aht_reduction = Blank("60% ↓ AHT\n(-$2.5M)")
        
    final_cost = Rack("Optimized OpEx\n($3.5M/yr)")

    current_cost >> deflection >> aht_reduction >> final_cost