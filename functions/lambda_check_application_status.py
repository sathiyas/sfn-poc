from __future__ import print_function

import json
import StackUtils
import requests

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"

    StackId = event['StackId']
    outputKey = event['outputKey']
    expectedVal = event['expectedVal']
    print (event)
    albDns = StackUtils.get_output(StackId,outputKey)
    url = 'http://' + albDns
    print (albDns)
    r = requests.get(url)
    print (r.content)
    if(expectedVal in r.content):
        return 'SUCCESS'
    #print r.headers
    #print r.content
