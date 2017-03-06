from __future__ import print_function

import json
import StackUtils
import urllib2

print('Loading function')


def lambda_handler(event, context):
    "This is the Lambda handler"
    print (event)
    StackId = event['StackId']
    outputKey = event['outputKey']
    expectedVal = event['expectedVal']
    print (event)
    albDns = StackUtils.get_output(StackId,outputKey)
    url = 'http://' + albDns
    print (albDns)
    #r = requests.get(url)
    #print (r.content)
    response = urllib2.urlopen(url).read()
    print (response)
    if(expectedVal in response):
        return getOutput("SUCCESS", StackId)
    else:
        return getOutput("FAILURE", StackId)

def getOutput(status, StackId):
    "This functions builds a JSON output"
    output = {}
    output['status'] = status
    output['StackId'] = StackId
    return output
