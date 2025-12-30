from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.database import Memorystore
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.storage import GCS

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Information Systems", show=False, filename="revrec_info_systems", direction="LR", graph_attr=graph_attr):
    rules = GCS("IFRS 15 Rulebook")
    
    with Cluster("IS Intelligence Layer"):
        faiss = Memorystore("FAISS Vector Index")
        agent_swarm = VertexAI("Multi-Agent Swarm")

    rules >> Edge(label="Vectorized", color="darkblue") >> faiss
    faiss >> Edge(label="Contextual RAG", color="darkgreen", style="bold") >> agent_swarm