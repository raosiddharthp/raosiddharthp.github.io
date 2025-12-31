from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack
from diagrams.generic.network import Router
graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}
with Diagram("Phase D: Telephony Ingress", show=False, filename="omni_telephony_map", direction="LR", graph_attr=graph_attr):
    with Cluster("Global Ingress"):
        pstn = Router("PSTN Gateway")
        glb = LoadBalancing("Regional Edge")
    with Cluster("Processing Backbone"):
        sip_gateway = Rack("Conversational AI\n(Dialogflow CX)")
        reasoning = VertexAI("Gemini 1.5 Flash\n(STT & Reasoning)")
    pstn >> glb >> sip_gateway >> reasoning