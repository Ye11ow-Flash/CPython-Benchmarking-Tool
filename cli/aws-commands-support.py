import sys
from pprint import pprint

import boto3

# client = boto3.client("ec2")
# Myec2 = client.describe_instances()
# for pythonins in Myec2["Reservations"]:
#     for printout in pythonins["Instances"]:
#         pprint(printout)


INSTANCE_ID: str = ""


def run_command(inst_id: str, *args) -> None:
    ssm_client = boto3.client("ssm")
    response = ssm_client.send_command(
        InstanceIds=[inst_id],
        DocumentName="AWS-RunShellScript",
        Parameters={"commands": [" ".join(args)]},
    )
    print(response)  # currently does work due to ssm missing in EC2 instance on aws


run_command(INSTANCE_ID, "echo", "hello world")
