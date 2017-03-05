from __future__ import print_function

import json
import StackUtils

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"

    StackId = event['StackId']
    print (event)
    status = StackUtils.describe_stacks(StackId)
    return status
