#This is to test Lambda function locally

import lambda_create_stack
reload(lambda_create_stack)

event = {}
context = None

event['KeyName'] = 'sathiyas'
event['VpcId'] = 'vpc-5bb8c53d'
event['SubnetIDs'] = 'subnet-15f06f29,subnet-5274661b'
event['stack_name'] = 'ecs-alb-stack'
event['S3_Url'] = 'https://s3.amazonaws.com/vageescof-code-artifacts/ecs-alb.yaml'
event['tag_name'] = 'Name'
event['tag_value'] = 'ecs-alb'
event['expectedVal'] = 'Congratulations'
event['outputKey'] = 'ECSALB'


output = lambda_create_stack.lambda_handler(event, context)
print 'Printing'
print (output)
