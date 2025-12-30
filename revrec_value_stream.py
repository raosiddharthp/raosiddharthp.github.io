from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("IFRS 15 Value Stream", show=False, filename="revrec_value_stream", direction="LR", graph_attr=graph_attr):
    step1 = Run("1. Identify Contract")
    step2 = Run("2. Perf Obligations")
    step3 = Run("3. Trans Price")
    step4 = Run("4. Allocation")
    step5 = Run("5. Recognition")

    agent = VertexAI("RevRec AI Agent\n(Validation)")

    step1 >> step2 >> step3 >> step4 >> step5
    [step2, step4, step5] >> Edge(color="darkblue", style="dashed") >> agent