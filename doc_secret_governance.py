from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.security import SecretManager, Iam
from diagrams.gcp.compute import Run
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Security: Secret Governance", show=False, filename="doc_secret_governance", direction="LR", graph_attr=graph_attr):
    sm = SecretManager("Secret Manager\n(HF / DocAI Keys)")
    iam = Iam("Least-Privilege\nService Account")
    worker = Run("Inference Worker")
    provider = Blank("External AI\nProviders")

    sm >> Edge(label="Inject") >> worker
    iam >> Edge(label="Authorize") >> worker
    worker >> Edge(label="Auth Request") >> provider