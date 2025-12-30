from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec XAI Drivers", show=False, filename="revrec_xai_drivers", direction="LR", graph_attr=graph_attr):
    decision = VertexAI("RevRec Decision\n(Recognize $1M)")

    with Cluster("Vertex Explainable AI"):
        term_length = Run("Term Length\n(60% Attribution)")
        user_count = Run("User Count\n(30% Attribution)")
        other = Run("Other Drivers\n(10%)")

    auditor = Run("Compliance Audit\nReport")

    decision >> Edge(label="ExplainRequest", color="darkblue") >> [term_length, user_count, other]
    [term_length, user_count] >> Edge(label="Justify", color="darkgreen") >> auditor