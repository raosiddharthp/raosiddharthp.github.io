from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Incident Response", show=False, filename="revrec_incident_response", direction="LR", graph_attr=graph_attr):
    drift = Monitoring("Model Drift Alert")
    outage = Monitoring("Regional Health Check")
    
    with Cluster("Automated Response"):
        router = Run("Traffic Rerouter")
        alert = Run("SRE PagerDuty")

    failover_site = Run("Secondary Region")
    manual_mode = Run("Manual Mode\n(Safe State)")

    drift >> router >> manual_mode
    outage >> router >> failover_site
    router >> alert