#This function sends a success for an Activity
#Pass the activity ARN in command line
import boto3
import sys

activityArn = sys.argv[1]

client = boto3.client("stepfunctions")
response = client.get_activity_task(
    activityArn=activityArn
)
token = response['taskToken']
response = client.send_task_success(
    taskToken=token,
    output='true'
)
