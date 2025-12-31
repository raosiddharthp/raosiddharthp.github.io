from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.devtools import GCR, Build
from diagrams.gcp.compute import Run
from diagrams.generic.network import Firewall

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("Supply Chain: Binary Auth", show=False, filename="doc_binary_auth", direction="LR", graph_attr=graph_attr):
    build = Build("Cloud Build\n(Vuln Scan)")
    registry = GCR("Container Registry")
    bin_auth = Firewall("Binary Authorization\n(Signed Attestor)")
    cloud_run = Run("Production Execution")
    build >> registry >> bin_auth >> cloud_run