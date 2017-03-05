#This python program is to create/delete a cloudformation stack
import boto3

client = boto3.client('cloudformation')

#Create stack
def create_stack(**kwarg):
    "This function creates a cloudformation stack"

    response = client.create_stack(
        StackName=kwarg['stack_name'],
        TemplateURL=kwarg['S3_Url'],
        Parameters=kwarg['parameters'],
        Capabilities=[
            'CAPABILITY_IAM'
        ],
        OnFailure='ROLLBACK',
        Tags=[
            {
                'Key': kwarg['tag_name'],
                'Value': kwarg['tag_value']
            }
        ]
    )
    return response['StackId']

#Delete stack
def delete_stack(stack_name):
    "This function deletes a cloudformation stack"
    client = boto3.client('cloudformation')
    response = client.delete_stack(
        StackName=stack_name
    )

#Describe stack
def describe_stacks(stack_id):
    "This functions describes a cloudformation stack and returns status"
    client = boto3.client('cloudformation')
    response = client.describe_stacks(
        StackName=stack_id
    )
    print "No of stacks: ", len(response['Stacks'])
    if len(response['Stacks']) == 1:
        StackStatus = response['Stacks'][0]['StackStatus']
        return StackStatus
    else:
        return "INVALID_STACK_ID"

#Describe stack
def get_output(stack_id, outputKey):
    "This functions describes a cloudformation stack and returns status"
    client = boto3.client('cloudformation')
    response = client.describe_stacks(
        StackName=stack_id
    )
    print "No of stacks: ", len(response['Stacks'])
    if len(response['Stacks']) == 1:
        Outputs = response['Stacks'][0]['Outputs']
        #print Outputs
        for output in Outputs:
            key = output['OutputKey']
            if(key == outputKey):
                return output['OutputValue']
    return None
