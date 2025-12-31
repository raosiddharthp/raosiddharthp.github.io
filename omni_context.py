from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Mobile
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.6", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("High-Level Context Diagram", show=False, filename="omni_context_diagram", direction="LR", graph_attr=graph_attr):
    user = Mobile("Customer\n(Voice/Chat)")
    
    with Cluster("Enterprise Sovereign AI"):
        brain = VertexAI("OmniMind Core\n(Gemini 1.5 Flash)")
        
    with Cluster("Record Systems"):
        crm = Rack("Salesforce/SAP")
        kb = Rack("Enterprise\nKnowledge Base")

    user >> Edge(label="Inquiry") >> brain
    brain >> Edge(label="Lookup", style="dashed") >> crm
    brain >> Edge(label="RAG", style="dashed") >> kb
    brain >> Edge(label="Resolution") >> user