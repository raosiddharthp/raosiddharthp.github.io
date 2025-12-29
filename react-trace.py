from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.operations import Monitoring

graph_attr = {
    "pad": "0.2",
    "nodesep": "1.2",
    "ranksep": "2.5",
    "bgcolor": "transparent"
}

with Diagram("ReAct Tool-Use Trace", show=False, filename="react-trace", direction="LR", graph_attr=graph_attr):
    
    pilot = VertexAI("Pilot Agent\n(Reasoning Core)")

    with Cluster("GCP-Native Tools (Action Space)"):
        billing_api = Monitoring("Billing API")
        carbon_api = Monitoring("Carbon API")

    # The ReAct Loop
    pilot >> Edge(label="1. Thought: Need Emissions Data", color="gray", style="dotted") >> pilot
    pilot >> Edge(label="2. Action: Call Carbon API", color="darkgreen", style="bold") >> carbon_api
    carbon_api >> Edge(label="3. Observation: Intensity High", color="darkgreen") >> pilot
    
    pilot >> Edge(label="4. Thought: Check Cost Threshold", color="gray", style="dotted") >> pilot
    pilot >> Edge(label="5. Action: Call Billing API", color="darkblue", style="bold") >> billing_api
    billing_api >> Edge(label="6. Observation: Under Budget", color="darkblue") >> pilot

    pilot >> Edge(label="7. Final Action: Trigger Shift", color="purple", style="bold") >> pilot