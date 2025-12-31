from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("C4 Component Diagram", show=False, filename="doc_c4_components", direction="TB", graph_attr=graph_attr):
    with Cluster("AI Orchestration Layer"):
        langchain = Blank("LangChain\n(Reasoning)")
        crewai = Blank("CrewAI\n(State Management)")
    
    with Cluster("Service Layer"):
        api = Run("FastAPI Wrapper")
        llm = VertexAI("Gemini Pro / HF")

    api >> langchain >> crewai >> llm