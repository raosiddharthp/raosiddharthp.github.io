from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Latency SLO", show=False, filename="revrec_latency_slo", direction="LR", graph_attr=graph_attr):
    trigger = Run("Contract Upload")
    
    with Cluster("Processing Target: < 30s (p95)"):
        unbundle = Run("AI Unbundling")
        validate = Run("Rule Validation")

    metrics = Monitoring("Latency SLO Monitor")

    trigger >> unbundle >> validate >> Edge(label="Log Timing") >> metrics