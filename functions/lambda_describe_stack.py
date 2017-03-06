from __future__ import print_function

import json
import StackUtils

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"
    print(event)
    #input = json.loads(event)
    StackId = event['StackId']
    expectedVal = event['expectedVal']
    outputKey = event['outputKey']
    print (StackId)
    status = StackUtils.describe_stacks(StackId)
    return getOutput(status, StackId, outputKey, expectedVal)

def getOutput(status, StackId, outputKey, expectedVal):
    "This functions builds a JSON output"
    output = {}
    output['status'] = status
    output['StackId'] = StackId
    output['outputKey'] = outputKey
    output['expectedVal'] = expectedVal
    return output
