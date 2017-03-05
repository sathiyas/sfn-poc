#This is to test Lambda function locally

import lambda_delete_stack

event = {}
context = None

event['stack_name'] = 'arn:aws:cloudformation:us-east-1:158369477098:stack/ecs-alb-stack/8bb1c4b0-01ae-11e7-9072-503f23fb559a'

lambda_delete_stack.lambda_handler(event, context)
