from diagrams import Diagram, Edge
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.ml import NaturalLanguageAPI, VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.2", "nodesep": "2.0", "ranksep": "3.0", "bgcolor": "transparent"}

with Diagram("ESG Lead Time Reduction", show=False, filename="esg_lead_time", direction="LR", graph_attr=graph_attr):
    ingest = Pubsub("Data Collection")
    process = Run("Validation Engine")
    ai_gen = VertexAI("AI Narrative Synth")
    audit = NaturalLanguageAPI("Final ESG Report")

    ingest >> Edge(label="Manual: 2 wks", color="red", style="dashed") >> process
    process >> Edge(label="AI: 2 mins", color="darkgreen", style="bold") >> ai_gen >> audit