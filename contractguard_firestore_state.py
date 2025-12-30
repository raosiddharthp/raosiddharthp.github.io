from diagrams import Diagram, Edge
from diagrams.gcp.database import Firestore
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Data Arch: Firestore State", show=False, filename="contractguard_firestore_state", direction="LR", graph_attr=graph_attr):
    swarm = Run("Negotiation Swarm\n(Agents)")
    state = Firestore("Firestore\n(State/Metadata)")
    
    swarm >> Edge(label="Sync State", color="darkorange") >> state