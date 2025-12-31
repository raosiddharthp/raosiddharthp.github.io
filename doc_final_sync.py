from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring, Logging
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack
graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}
with Diagram("SRE: Performance Dashboard", show=False, filename="doc_sre_dashboard", direction="LR", graph_attr=graph_attr):
    [Monitoring("Cloud Monitoring"), Logging("Cloud Logging"), Rack("Cloud Trace\n(Audit IDs)")] >> Rack("R Shiny Dashboard")
with Diagram("Governance: Audit Lineage", show=False, filename="doc_audit_lineage", direction="LR", graph_attr=graph_attr):
    i, p, s, a = GCS("Raw Document"), Run("Process Worker"), BigQuery("Structured Output"), Rack("Audit Trace")
    i >> Edge(label="Process") >> p >> Edge(label="Store") >> s
    a >> Edge(style="dashed", label="Correlate") >> [i, p, s]