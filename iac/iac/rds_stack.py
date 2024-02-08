import os

from aws_cdk import (
    CfnOutput, aws_cognito,
    aws_rds as rds,
)
from constructs import Construct


class RDSStack(Construct):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "EurekaRDSStack")


