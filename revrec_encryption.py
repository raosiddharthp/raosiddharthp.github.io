from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.security import KeyManagementService
from diagrams.gcp.database import SQL
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Field-Level Encryption", show=False, filename="revrec_encryption", direction="LR", graph_attr=graph_attr):
    kms = KeyManagementService("Cloud KMS\n(CMEK)")
    
    with Cluster("Encrypted at Rest"):
        db = SQL("Cloud SQL\n(Ciphertext PII)")

    agent = VertexAI("Authorized Agent\n(Decryption in RAM)")

    db >> Edge(label="Pull Ciphertext", color="gray") >> agent
    kms >> Edge(label="DEK Decrypt", color="darkgreen", style="bold") >> agent
    agent >> Edge(label="Process Plaintext", color="darkblue") >> agent