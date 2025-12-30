from diagrams import Diagram, Edge
from diagrams.gcp.analytics import Pubsub, BigQuery
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Future State", show=False, filename="revrec_future_state", direction="LR", graph_attr=graph_attr):
    trigger = Pubsub("Contract Signed\nEvent")
    agent = VertexAI("RevRec-AI\n(Policy Logic)")
    ledger = BigQuery("Cloud ERP / Ledger\n(Automated Post)")

    trigger >> Edge(label="Auto-Trigger", color="darkgreen", style="bold") >> agent >> Edge(label="Direct GL Post", color="darkgreen") >> ledger