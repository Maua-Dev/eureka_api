from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_ecs as ecs,
)
from constructs import Construct


class NetworkStack(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, "EurekaNetworkStack")

        # Our network in the cloud
        self.vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=2,  # default is all AZs in region
            nat_gateways=0,  # No Nat GWs are required as we will add VPC endpoints
            enable_dns_hostnames=True,
            enable_dns_support=True,
        )
        self.ecs_cluster = ecs.Cluster(self, f"ECSCluster", vpc=self.vpc)
        # Add VPC endpoints to keep the traffic inside AWS


