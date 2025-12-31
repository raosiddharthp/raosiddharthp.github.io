from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.vcs import Github
from diagrams.onprem.iac import Terraform
from diagrams.gcp.compute import Run
from diagrams.gcp.security import Iam

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("CI/CD: Terraform Governance", show=False, filename="doc_terraform_pipeline", direction="LR", graph_attr=graph_attr):
    code = Github("IaC Repo")
    plan = Terraform("Plan & Sentinel\nPolicies")
    
    with Cluster("Target Environment"):
        infra = Run("Serverless Stack")
        policy = Iam("Least-Privilege\nIAM")

    code >> plan >> [infra, policy]