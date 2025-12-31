from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.6", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase C: Multi-Agent Sequence", show=False, filename="omni_agent_sequence", direction="TB", graph_attr=graph_attr):
    user = Blank("User Inquiry")
    
    with Cluster("Agent Swarm (Vertex AI)"):
        orchestrator = VertexAI("Orchestrator\n(Intent/Routing)")
        knowledge = VertexAI("Knowledge Agent\n(RAG/Vector)")
        action = VertexAI("Action Agent\n(API/Tool Use)")

    user >> Edge(label="Input") >> orchestrator
    orchestrator >> Edge(label="Lookup") >> knowledge
    knowledge >> Edge(label="Context") >> orchestrator
    orchestrator >> Edge(label="Execute") >> action
    action >> Edge(label="Result") >> orchestrator
    orchestrator >> Edge(label="Response") >> user