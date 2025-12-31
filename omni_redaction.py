from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI
from diagrams.generic.network import Firewall
graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}
with Diagram("Compliance: Redaction Flow", show=False, filename="omni_redaction_flow", direction="LR", graph_attr=graph_attr):
    raw_data = Run("Audio/Chat\nIngestion")
    scrubber = Firewall("Cloud DLP\n(PII Scrubber)")
    with Cluster("Sovereign Storage"):
        masked_bq = BigQuery("Redacted Logs")
        llm = VertexAI("Gemini 1.5\n(Clean Context)")
    raw_data >> scrubber >> [masked_bq, llm]