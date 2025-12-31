from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.network import VirtualPrivateCloud

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Physical Arch: VPC-SC Perimeter", show=False, filename="doc_vpcsc_perimeter", direction="LR", graph_attr=graph_attr):
    with Cluster("VPC Service Perimeter"):
        source = GCS("Ingestion Bucket\n(Encrypted)")
        worker = Run("Extraction Agent\n(Cloud Run)")
        model = VertexAI("Llama-3/Gemini\nEndpoint")
        
    source >> Edge(label="Eventarc") >> worker >> Edge(label="Private API") >> model