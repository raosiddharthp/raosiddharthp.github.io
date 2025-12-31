from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.compute import Functions, Run
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Event-Driven Agentic Orchestration", show=False, filename="doc_agentic_orchestration", direction="LR", graph_attr=graph_attr):
    source = GCS("Raw Document\n(Upload)")
    with Cluster("Serverless Event Layer"):
        event_trigger = Functions("Cloud Function\n(Eventarc)")
        bus = Pubsub("Document Pipeline\n(Pub/Sub)")
    with Cluster("Agent Swarm (Cloud Run)"):
        classifier = VertexAI("Classifier Agent")
        extractor = VertexAI("Extraction Agent")
    destination = Rack("Structured Metadata\n(BigQuery)")
    source >> Edge(label="Finalize") >> event_trigger >> bus >> classifier >> extractor >> destination