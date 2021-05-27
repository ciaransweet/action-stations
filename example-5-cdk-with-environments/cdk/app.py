#!/usr/bin/env python3
import os

from aws_cdk import core
from example_stack import ExampleStack

app = core.App()

identifier = os.environ["IDENTIFIER"]

ExampleStack(
    scope=app,
    construct_id=f"action-stations-example-5-{identifier}",
    identifier=identifier,
)

for k, v in {
    "Project": "action-stations",
    "Stack": identifier,
    "Client": "Development Seed",
    "Owner": os.environ["OWNER"],
}.items():
    core.Tags.of(app).add(k, v, apply_to_launched_instances=True)

app.synth()
