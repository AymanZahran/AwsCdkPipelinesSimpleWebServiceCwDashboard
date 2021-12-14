from constructs import Construct
from aws_cdk import (
    Stage
)

from SimpleWebServiceStack import SimpleWebServiceStack

class SimpleWebServiceStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = SimpleWebServiceStack(self, 'SimpleWebServiceStack')