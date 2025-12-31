from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Monitoring
from diagrams.generic.device import Tablet
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase G: Governance Kill Switch", 
    show=False, 
    filename="risk_governance_killswitch", 
    direction="LR", 
    graph_attr=graph_attr
):
    agent = VertexAI("Risk Agent Swarm\n(Recommender)")
    risk_score = Monitoring("High Risk Signal\n(Confidence Check)")
    
    with Cluster("HITL Governance Gate"):
        compliance_user = Tablet("Compliance Officer\n(Manual Review)")
        signature = Rack("Digital Audit Record\n(Signature)")

    action = Rack("Close/Escalate Case")

    agent >> risk_score
    risk_score >> Edge(label="Requires Review", color="darkred", style="bold") >> compliance_user
    compliance_user >> signature >> action