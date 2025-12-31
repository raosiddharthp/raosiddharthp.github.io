from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank
from diagrams.gcp.analytics import Pubsub

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Business Transformation Roadmap", show=False, filename="omni_transformation_readiness", direction="LR", graph_attr=graph_attr):
    legacy = Blank("Legacy IVR\n(Static Silos)")
    bridge = Pubsub("Hybrid Integration\n(Dialogflow CX)")
    target = Blank("Agentic OmniMind\n(Gemini Orchestrator)")

    legacy >> Edge(label="Digital Debt", color="darkred") >> bridge >> Edge(label="Value Realization", color="darkgreen", style="bold") >> target