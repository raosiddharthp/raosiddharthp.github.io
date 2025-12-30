from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Enabled Value Stream", show=False, filename="revrec_enabled_stream", direction="LR", graph_attr=graph_attr):
    with Cluster("IFRS 15 Pipeline"):
        contract = Run("1. Contract ID")
        obligations = Run("2. Perf Obligations")
        price = Run("3. Trans Price")
        alloc = Run("4. Allocation")
        recog = Run("5. Recognition")

    ai_agent = VertexAI("Predictive RevRec-AI")

    contract >> obligations >> price >> alloc >> recog
    ai_agent >> Edge(label="Real-time Validation", color="purple") >> [obligations, recog]