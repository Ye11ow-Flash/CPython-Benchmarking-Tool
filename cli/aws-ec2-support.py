import sys
from pprint import pprint

# Instance Id
import boto3
from paramiko import SSHClient
from scp import SCPClient

client = boto3.client("ec2")
Myec2 = client.describe_instances()
for pythonins in Myec2["Reservations"]:
    for printout in pythonins["Instances"]:
        pprint(printout)

        # Send script via SCP - "scp -i cpython.pem <path_to_script_file> ec2-user@ec2-3-89-101-123.compute-1.amazonaws.com:~/."
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect("ec2-user@ec2-3-89-101-123.compute-1.amazonaws.com:~/.")
        with SCPClient(ssh.get_transport()) as scp:
            scp.put("script.py", "script.py")

        # Send command to execute the script
        commands = ["python3 script.py"]
        instance_ids = [printout]
        # execute_commands_on_linux_instances(client, commands, instance_ids)
