from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("GreenOps Agentic Swarm", show=False, filename="greenops-swarm", direction="LR", graph_attr=graph_attr):
    
    supervisor = VertexAI("Swarm Supervisor\n(Orchestration Logic)")

    with Cluster("Specialized Worker Agents"):
        billing_agent = Run("Cost Analyst Agent")
        carbon_agent = Run("Emissions Analyst Agent")
        steering_agent = Run("Optimization Agent")

    # Horizontal Orchestration
    supervisor >> Edge(label="Delegate Task", color="darkblue") >> billing_agent
    supervisor >> Edge(color="darkblue") >> carbon_agent
    supervisor >> Edge(color="darkblue") >> steering_agent

    # Handoffs back to Supervisor for state update
    [billing_agent, carbon_agent, steering_agent] >> Edge(label="State Update", color="darkgreen", style="dashed") >> supervisor