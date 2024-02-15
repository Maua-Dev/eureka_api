import os

from aws_cdk import (
    CfnOutput, aws_cognito,
    aws_rds as rds,
    RemovalPolicy,
    aws_ec2 as ec2,


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
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            credentials=rds.Credentials.from_generated_secret("postgres"),
            removal_policy=RemovalPolicy.DESTROY,
            database_name="eureka",
            publicly_accessible=True,
        )


