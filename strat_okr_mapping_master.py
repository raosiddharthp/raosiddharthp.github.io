from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack
from diagrams.gcp.analytics import Looker

# TOGAF Phase B: Business Architecture - OKR Alignment
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase B: OKR Real-Time Mapping", 
    show=False, 
    filename="strat_okr_mapping_master", 
    direction="TB", 
    graph_attr=graph_attr
):
    # Strategic Board-Level Objectives
    with Cluster("Strategic Themes (Board-Level)"):
        cfo_theme = Blank("Predictable Revenue")
        cto_theme = Blank("Engineering Velocity")
        cso_theme = Blank("Data Sovereignty")

    # Mid-Tier Execution (SAFe ARTs)
    with Cluster("Agile Release Trains (ARTs)"):
        art_fin = Rack("FinOps & RevRec ART")
        art_core = Rack("Cloud Native Platform ART")
        art_sec = Rack("Zero-Trust Security ART")

    # Technical Metrics Flowing Up
    metrics_hub = Looker("Real-Time OKR Dashboard")

    # Mapping Logic
    cfo_theme >> Edge(color="darkblue") >> art_fin
    cto_theme >> Edge(color="darkgreen") >> art_core
    cso_theme >> Edge(color="darkred") >> art_sec

    [art_fin, art_core, art_sec] >> Edge(label="Live Performance Data") >> metrics_hub