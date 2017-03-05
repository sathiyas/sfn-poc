#This is to test Lambda function locally

import lambda_check_application_status

event = {}
context = None

event['StackId'] = 'arn:aws:cloudformation:us-east-1:158369477098:stack/ecs-alb-stack/741785e0-01b0-11e7-9fcc-50d5ca63261e'
event['outputKey'] = 'ECSALB'
event['expectedVal'] = 'Congratulations'
#event['StackId'] = 'ecs-alb-stack'

retVal = lambda_check_application_status.lambda_handler(event, context)
print (retVal)
