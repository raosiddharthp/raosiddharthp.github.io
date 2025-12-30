from diagrams import Diagram, Edge
from diagrams.gcp.database import Memorystore
from diagrams.gcp.ml import NaturalLanguageAPI

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Data Arch: FAISS Vector DB", show=False, filename="contractguard_faiss_vector", direction="LR", graph_attr=graph_attr):
    embeddings = NaturalLanguageAPI("Semantic Embeddings")
    vector_store = Memorystore("FAISS Vector DB\n(Legal Playbook)")
    
    embeddings >> Edge(label="Vectorize", color="darkblue") >> vector_store