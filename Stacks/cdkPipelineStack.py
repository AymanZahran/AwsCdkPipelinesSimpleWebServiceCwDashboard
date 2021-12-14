from aws_cdk import (
    # Duration,
    Stack,
    pipelines as pipelines,
    aws_secretsmanager as secretsmanager,
)
from constructs import Construct

from SimpleWebServiceStage import SimpleWebServiceStage

class cdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        GITHUB_REPO = "AymanZahran/AWSAutomationWithCDK"

        # Pipeline code goes here
        pipeline = pipelines.CodePipeline(
            self,
            "cdkPipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.git_hub(GITHUB_REPO, "main"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "npx cdk synth",
                ]
            ),
        )

        WebServiceStage = SimpleWebServiceStage(self, "SimpleWebServiceStage")
        Launch_WebService = pipeline.add_stage(WebServiceStage)