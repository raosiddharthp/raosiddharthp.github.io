from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Monitoring

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Information Architecture Lineage", show=False, filename="data_lineage", direction="LR", graph_attr=graph_attr):
    with Cluster("Raw Telemetry Sources"):
        src_billing = Monitoring("GCP Billing API\n(Cost Inflow)")
        src_carbon = Monitoring("Carbon Footprint API\n(Emissions Inflow)")

    with Cluster("Governance & Storage Layer"):
        lake = BigQuery("Sustainability Lake")
        governance = DataCatalog("Data Lineage\n& Tagging")

    # Reporting Layer
    report = VertexAI("Gemini Narrative\n(ESG Report Synth)")

    # Logical Data Flow
    src_billing >> Edge(color="darkblue") >> lake
    src_carbon >> Edge(color="darkgreen") >> lake
    lake >> Edge(label="Enriched Context", style="bold") >> report
    lake - governance