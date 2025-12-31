from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow
from diagrams.gcp.compute import Run
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Operational: Real-Time Flow", show=False, filename="gov_event_driven_workflow", direction="LR", graph_attr=graph_attr):
    source = Rack("External Data")
    bus = Pubsub("Governance Topics")
    with Cluster("Real-Time Processing"):
        proc = Dataflow("Validation Pipeline")
        swarm = Run("Agent Swarm\n(Cloud Run)")
    catalog = Storage("Enterprise Catalog\n(Dataplex)")
    source >> bus >> proc >> swarm >> catalog