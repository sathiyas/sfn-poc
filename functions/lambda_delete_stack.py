from __future__ import print_function

import json
import StackUtils

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"

    StackName = event['stack_name']
    print (event)
    StackUtils.delete_stack(StackName)
