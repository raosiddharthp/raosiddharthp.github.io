from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import NaturalLanguageAPI, VertexAI
from diagrams.gcp.compute import Run
from diagrams.gcp.analytics import BigQuery
from diagrams.generic.device import Tablet

# Diagram configuration for Gold Standard horizontal (LR) flow
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "fontname": "Sans-Serif",
    "fontsize": "15"
}

with Diagram(
    "TOGAF Value Stream: Legal Friction to Bottom Line Impact",
    show=False,
    filename="contractguard_value_stream_impact",
    direction="LR",
    graph_attr=graph_attr
):
    
    # Value Stream Stage 1: Inception
    contract_in = Tablet("Contract Ingestion\n(Legal Friction)")

    with Cluster("Value Add Stage: Automated Risk Extraction"):
        # TOGAF Phase C: Information Systems intervention
        nlp_engine = NaturalLanguageAPI("NLP Clause Parser")
        risk_matrix = VertexAI("Indemnity Risk\nScoring")
        
    with Cluster("Value Add Stage: Business Decisioning"):
        # TOGAF Phase B: Business Architecture acceleration
        counsel_review = Run("Counsel Approval\n(Accelerated)")
        audit_ready = BigQuery("SOX Compliant\nRecord")

    # Final Value Realization
    impact = Run("Bottom Line Impact:\nRevenue Realization")

    # Defining the Value Flow
    contract_in >> Edge(label="Unstructured Data", color="darkred") >> nlp_engine
    nlp_engine >> risk_matrix
    risk_matrix >> Edge(label="Validated Risk", color="darkgreen", style="bold") >> counsel_review
    counsel_review >> audit_ready >> Edge(label="Realized Value", color="darkblue", style="bold") >> impact

    # Framework Annotation: Note on SAFe/TOGAF alignment
    # In a live portfolio, this diagram demonstrates the elimination of 
    # manual 'Judgment Bottlenecks' identified in Phase B.