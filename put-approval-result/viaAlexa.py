#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

# A function to find a key's value given a dictionary
def key_search(data, target_key):
    if type(data) == list:
        for item in data:
            res = key_search(item, target_key)
            if res:
                return res
    elif type(data) == dict:
        for key, val in data.items():
            if key == target_key:
                return val
            else:
                res = key_search(val, target_key)
                if res:
                    return res
    return None

# Lambda function to return result to Alexa
def lambda_handler(event, context):
    # Initiate the Pipeline Client
    pipelineClient = boto3.client('codepipeline')

    # The Pipeline to Work With
    myPipeline = 'YOUR_PIPELINE_NAME'
    myStage = 'YOUR_STAGE'
    myAction = 'YOUR_ACTION'

    # The State of the Pipeline
    state = pipelineClient.get_pipeline_state(name=myPipeline)

    # Get the token value of the approval step
    myToken = key_search(state, 'token')

    if myToken is None:
        return {'version': '1.0', 'shouldEndSession': True, 'response': {'outputSpeech': {'text': 'No builds waiting',
                'type': 'PlainText'}}}
    else:
        pipelineClient.put_approval_result(pipelineName=myPipeline, stageName=myStage, actionName=myAction,
                                           result={'summary': 'Approved via lambda IoT', 'status': 'Approved'},
                                           token=myToken)

    return {'version': '1.0', 'shouldEndSession': True,
            'response': {'outputSpeech': {'text': 'Your deployment has been approved', 'type': 'PlainText'}}}
