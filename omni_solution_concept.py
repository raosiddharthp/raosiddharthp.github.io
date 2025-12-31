from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Tablet
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.6", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("OmniMind Solution Concept", show=False, filename="omni_solution_concept", direction="LR", graph_attr=graph_attr):
    user = Tablet("Customer Interaction\n(Omni-Channel)")
    
    with Cluster("The OmniMind Brain"):
        orchestrator = VertexAI("Gemini 1.5 Orchestrator\n(Logic & Routing)")
        
    with Cluster("Legacy Integration Fabric"):
        crm = Rack("CRM (Salesforce/SAP)")
        billing = Rack("Legacy Billing")
        mainframe = Rack("Core Mainframe")

    user >> Edge(label="Request") >> orchestrator
    orchestrator >> Edge(label="Stateful Query", style="dashed") >> [crm, billing, mainframe]
    orchestrator >> Edge(label="Governed Response") >> user