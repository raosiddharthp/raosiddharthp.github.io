from diagrams import Diagram, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.search import Search

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Governance: Audit Lineage", show=False, filename="doc_audit_lineage", direction="LR", graph_attr=graph_attr):
    ingest = GCS("Raw Document")
    proc = Run("Process Worker")
    store = BigQuery("Structured Output")
    audit = Search("Unique Request ID\n(Audit Trace)")
    ingest >> Edge(label="Process") >> proc >> Edge(label="Store") >> store
    audit >> Edge(style="dashed", label="Correlate") >> [ingest, proc, store]