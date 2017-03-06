#This is to test Lambda function locally

import lambda_describe_stack
import json

event = {}
context = None

input = {"StackId": "arn:aws:cloudformation:us-east-1:158369477098:stack/ecs-alb-stack/741785e0-01b0-11e7-9fcc-50d5ca63261e"}

event['StackId'] = 'arn:aws:cloudformation:us-east-1:158369477098:stack/ecs-alb-stack/741785e0-01b0-11e7-9fcc-50d5ca63261e'
event['expectedVal'] = 'Congratulations'
event['outputKey'] = 'ECSALB'
#event['StackId'] = 'ecs-alb-stack'

#StackStatus = lambda_describe_stack.lambda_handler(json.dumps(input), context)
StackStatus = lambda_describe_stack.lambda_handler(event, context)

print 'StackStatus ', StackStatus
