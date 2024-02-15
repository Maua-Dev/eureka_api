import os
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    CfnOutput,
    aws_iam as iam,
    SecretValue, aws_ecr, RemovalPolicy
)
from constructs import Construct
from aws_cdk.aws_cloudwatch import ComparisonOperator
from aws_cdk.aws_sns import Topic

from aws_cdk.aws_cloudwatch_actions import SnsAction

from .fargate_stack import FargateStack
from .network_stack import NetworkStack
from .rds_stack import RDSStack


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.aws_account_id = os.environ.get("AWS_ACCOUNT_ID")
        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.project_name = os.environ.get("PROJECT_NAME")

        REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref_name else RemovalPolicy.DESTROY


        self.network_stack = NetworkStack(self, "EurekaNetworkStack")

        self.rds_stack = RDSStack(self, self.network_stack.vpc)

        self.fargate_stack = FargateStack(self, "EurekaFargateStack", vpc=self.network_stack.vpc,
                                          ecs_cluster=self.network_stack.ecs_cluster)
