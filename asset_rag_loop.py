from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.database import Memorystore
from diagrams.generic.device import Tablet
from diagrams.gcp.storage import GCS

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.0",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "MLE View: Agentic RAG Loop", 
    show=False, 
    filename="asset_rag_loop", 
    direction="LR", 
    graph_attr=graph_attr
):
    user_query = Tablet("Analyst Query")
    
    with Cluster("Reasoning Engine"):
        agent = VertexAI("Reasoning Agent\n(Gemini 1.5 Pro)")
        
    with Cluster("Grounded Context"):
        vector_search = Memorystore("Vector Retrieval")
        enterprise_docs = GCS("Enterprise Knowledge")

    user_query >> agent
    agent >> Edge(label="Semantic Search", color="darkblue") >> vector_search
    vector_search >> Edge(label="Retrieve Slabs") >> enterprise_docs
    enterprise_docs >> Edge(label="Context Injection", color="darkgreen") >> agent
    agent >> Edge(label="Grounded Response") >> user_query