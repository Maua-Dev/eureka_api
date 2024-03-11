import os

from aws_cdk import (
    CfnOutput, aws_cognito,
    aws_rds as rds,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_secretsmanager as secretsmanager


)
from constructs import Construct


class RDSStack(Construct):
    def __init__(self, scope: Construct, vpc: ec2.Vpc) -> None:
        super().__init__(scope, "EurekaRDSStack")


        # create random secret for RDS
        self.secret = secretsmanager.Secret(
            self,
            "EurekaRDSInstanceSecret",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                exclude_punctuation=True
            ),
        )


        self.rds = rds.DatabaseInstance(
            self,
            "RDS",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_12
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            credentials=rds.Credentials.from_secret(self.secret),
            removal_policy=RemovalPolicy.DESTROY,
            database_name="eureka",
            publicly_accessible=True,
        )


