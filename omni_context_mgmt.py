from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.gcp.storage import GCS

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Phase C: Context Management", show=False, filename="omni_context_mgmt", direction="LR", graph_attr=graph_attr):
    history = GCS("Historical Interactions\n(Long-Term Memory)")
    
    with Cluster("Gemini 2M Context Window"):
        current = Blank("Live Session Tokens")
        retrieved = Blank("Retrieved Context\n(Previous Calls)")
        reasoning = Blank("Cross-Turn\nReasoning")

    output = Blank("Hyper-Personalized\nResponse")

    history >> retrieved
    [current, retrieved] >> reasoning >> output