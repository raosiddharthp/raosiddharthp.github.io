from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.iot import IotCore
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram("Data Lineage & Audit Map", show=False, filename="audit_map", direction="LR", graph_attr=graph_attr):
    
    raw_metric = IotCore("Raw Carbon\nMetric (gCO2/kWh)")

    with Cluster("Transformation & Governance"):
        logic = BigQuery("Standardization\nLogic")
        lineage = DataCatalog("Audit Trail\n(Lineage Tag)")

    agent_logic = VertexAI("Optimization\nPolicy Engine")
    action = Run("Agentic Shifting\nAction (Trigger)")

    # Lineage Flow
    raw_metric >> Edge(label="Ingested", color="gray") >> logic
    logic >> Edge(label="Validated", color="darkgreen") >> agent_logic
    agent_logic >> Edge(label="Authorized", color="purple", style="bold") >> action
    
    # Audit connection
    logic - lineage
    agent_logic - lineage