from diagrams import Diagram, Cluster, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase B: Value Stream Coordination", show=False, filename="strat_value_stream_coord", direction="TB", graph_attr=graph_attr):
    
    with Cluster("Strategic Themes"):
        theme1 = Blank("Financial Predictability")
        theme2 = Blank("Digital Sovereignty")

    with Cluster("Value Streams / ARTs"):
        art_ai = Rack("ART: Intelligence Engine")
        art_sec = Rack("ART: Global Security")
        art_ops = Rack("ART: Cloud Ops")

    theme1 >> [art_ai, art_ops]
    theme2 >> art_sec
    
    [art_ai, art_sec, art_ops] >> Edge(label="Value Realization") >> Blank("Enterprise Market Share")