from __future__ import print_function

import json
import StackUtils

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"

    StackId = event['StackId']
    print (event)
    StackUtils.delete_stack(StackId)
    return getOutput(StackId)

def getOutput(StackId):
    "This functions builds a JSON output"
    output = {}
    output['StackId'] = StackId
    output['expectedVal'] = "N/A"
    output['outputKey'] = "N/A"
    return output
