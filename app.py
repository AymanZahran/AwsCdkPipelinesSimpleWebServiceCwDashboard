#!/usr/bin/env python3
import os

import aws_cdk as cdk

from Stacks.cdkPipelineStack import cdkPipelineStack


app = cdk.App()
cdkPipelineStack(app, "cdkPipelineStack")

app.synth()
