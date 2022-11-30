import sys
from pprint import pprint

# Instance Id
import boto3

client = boto3.client("ec2")
Myec2 = client.describe_instances()
for pythonins in Myec2["Reservations"]:
    for printout in pythonins["Instances"]:
        pprint(printout)


# print(sys.argv)
# ec2 = boto3.client("ec2")

# response = ec2.describe_instances()


# print(dir(ec2))

# print(ec2._client_config)

# print("here 3")
# print(response)


# import re

# # mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo", "catfish"]
# r = re.compile(".*")  # aws_access_key_id
# # newlist = list(filter(r.match, mylist))  # Read Note below
# # print(newlist)
# print([val for val in dir(ec2) if r.match(val)])
