from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.5", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase 2: Intelligent Tagging", show=False, filename="gov_phase2_tagging", direction="LR", graph_attr=graph_attr):
    meta = Rack("Data Catalog")
    nlp = VertexAI("spaCy/Vertex AI")
    drift = Rack("Drift Alerts")
    
    meta >> nlp >> drift