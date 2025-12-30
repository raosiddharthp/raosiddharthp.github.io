from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Circuit Breaker", show=False, filename="revrec_circuit_breaker", direction="LR", graph_attr=graph_attr):
    stream = Run("Contract Stream")
    
    with Cluster("Confidence Threshold Guard"):
        ai = VertexAI("Inference Engine")
        monitor = Monitoring("Confidence Check")

    manual_queue = Run("Manual Controller\nReview Queue")
    ledger = Run("Automated Ledger Post")

    stream >> ai >> monitor
    monitor >> Edge(label="Confidence < 95%", color="red", style="bold") >> manual_queue
    monitor >> Edge(label="Safe", color="darkgreen") >> ledger