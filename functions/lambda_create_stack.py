from __future__ import print_function

import json
import StackUtils

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"

    StackName = event['stack_name']
    status = StackUtils.describe_stacks(StackName)
    if(status == 'CREATE_COMPLETE'):
        print ('Stack already exists')
        return StackUtils.getStackId(StackName)

    KeyName = event['KeyName']
    VpcId = event['VpcId']
    SubnetIDs = event['SubnetIDs']
    S3_Url = event['S3_Url']
    tag_name = event['tag_name']
    tag_value = event['tag_value']

    KeyName_param = {}
    KeyName_param['ParameterKey'] = 'KeyName'
    KeyName_param['ParameterValue'] = KeyName
    VpcId_param = {}
    VpcId_param['ParameterKey'] = 'VpcId'
    VpcId_param['ParameterValue'] = VpcId
    SubnetIDs_param = {}
    SubnetIDs_param['ParameterKey'] = 'SubnetID'
    SubnetIDs_param['ParameterValue'] = SubnetIDs
    parameters = [KeyName_param,VpcId_param,SubnetIDs_param]
    print (parameters)
    print (event)
    stackId = StackUtils.create_stack(stack_name=StackName,S3_Url=S3_Url,parameters=parameters,tag_name=tag_name,tag_value=tag_value)
    return stackId
