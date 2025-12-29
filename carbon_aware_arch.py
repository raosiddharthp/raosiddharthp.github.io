from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Monitoring

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Carbon-Aware Architecture", show=False, filename="carbon_aware_arch", direction="LR", graph_attr=graph_attr):

    with Cluster("Data Inputs"):
        billing = Monitoring("Cloud Billing API\n(Cost Data)")
        carbon = VertexAI("Carbon API\n(Emissions Data)")

    # The central brain
    agent_builder = VertexAI("Vertex AI\nAgent Builder")
    data_lake = BigQuery("Sustainability\nData Warehouse")

    optimization = Run("Carbon-Aware\nOptimizer Agent")

    # Horizontal Orchestration
    billing >> Edge(color="darkblue") >> data_lake
    carbon >> Edge(color="darkgreen") >> data_lake
    
    data_lake >> Edge(label="Training/Context") >> agent_builder
    agent_builder >> Edge(label="Orchestrate", style="bold", color="darkgreen") >> optimization