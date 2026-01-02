from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.security import IAP, KeyManagementService
from diagrams.gcp.operations import Monitoring, Logging
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack
from diagrams.generic.network import Firewall

graph_attr = {
    "pad": "0.3",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "bgcolor": "transparent",
    "fontname": "Sans-serif"
}

with Diagram("The Autonomous Enterprise: Sovereign Fabric", show=False, filename="ae_master_blueprint", direction="TB", graph_attr=graph_attr):
    user = Rack("Omni-Channel Ingress")
    iap = IAP("Zero-Trust Gate (IAP)")

    with Cluster("Enterprise Security Perimeter (VPC-SC)"):
        vpc_sc = Firewall("VPC Service Controls")
        
        with Cluster("Shared Service Layer"):
            gemini = VertexAI("Gemini 1.5 Orchestrator")
            registry = Rack("Agent Registry")
            
        with Cluster("Agile Release Trains (Value Streams)"):
            finance = Run("Finance ART")
            legal = Run("Legal ART")
            cx = Run("CX ART")

        with Cluster("Data & Governance Fabric"):
            kms = KeyManagementService("Cloud KMS")
            audit = Logging("Centralized Audit")
            metrics = Monitoring("Real-time SRE")

    user >> iap >> vpc_sc >> gemini
    gemini >> Edge(color="darkblue") >> [finance, legal, cx]
    for node in [finance, legal, cx, gemini]:
        node >> Edge(style="dashed") >> [audit, metrics]
    kms >> Edge(style="dotted") >> [finance, legal, cx]