from diagrams import Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.5", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Phase 3: Agentic Autonomy", show=False, filename="gov_phase3_agentic", direction="LR", graph_attr=graph_attr):
    logic = Blank("LangChain Core")
    agent = Run("Governance Agent")
    action = Run("Sub-5s Validation")
    
    logic >> agent >> action