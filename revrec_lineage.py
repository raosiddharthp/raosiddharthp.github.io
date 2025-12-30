from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Data Lineage", show=False, filename="revrec_lineage", direction="LR", graph_attr=graph_attr):
    raw_pdf = GCS("Contract PDF\n(Source)")
    
    with Cluster("Agentic Transformation"):
        ocr_agent = VertexAI("OCR & Extraction")
        rule_engine = VertexAI("IFRS 15 Logic")
        catalog = DataCatalog("Data Lineage Metadata")

    journal_entry = BigQuery("General Ledger\n(Journal Entry)")

    raw_pdf >> ocr_agent >> rule_engine >> journal_entry
    [ocr_agent, rule_engine, journal_entry] >> Edge(color="purple", style="dotted") >> catalog