import os

from aws_cdk import (
    CfnOutput, aws_cognito,
    aws_rds as rds,
    RemovalPolicy

)
from constructs import Construct


class RDSStack(Construct):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "EurekaRDSStack")

        self.rds = rds.DatabaseInstance(
            self,
            "RDS",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15_2
            ),
            instance_type=rds.InstanceType.of(
                rds.InstanceClass.BURSTABLE2, rds.InstanceSize.MICRO
            ),
            credentials=rds.Credentials.from_generated_secret("postgres"),
            removal_policy=RemovalPolicy.DESTROY,
            database_name="eureka",
            publicly_accessible=True,
        )


