from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring, Logging
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

# SRE Dashboard Logic
with Diagram("SRE: Performance Dashboard", show=False, filename="doc_sre_dashboard", direction="LR", graph_attr=graph_attr):
    metrics = Monitoring("Cloud Monitoring")
    logs = Logging("Cloud Logging")
    trace = Rack("Cloud Trace\n(Audit IDs)")
    dashboard = Rack("R Shiny Dashboard")
    [metrics, logs, trace] >> dashboard

# Audit Lineage Logic
with Diagram("Governance: Audit Lineage", show=False, filename="doc_audit_lineage", direction="LR", graph_attr=graph_attr):
    ingest = GCS("Raw Document")
    proc = Run("Process Worker")
    store = BigQuery("Structured Output")
    audit = Rack("Unique Request ID\n(Audit Trace)")
    ingest >> Edge(label="Process") >> proc >> Edge(label="Store") >> store
    audit >> Edge(style="dashed", label="Correlate") >> [ingest, proc, store]