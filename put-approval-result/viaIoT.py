#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

# A function to return a key value given a dictionary
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

# A Lambda function to be called by IoT button press
def lambda_handler(event, context):
    # Initiate the Pipeline Client
    pipelineClient = boto3.client('codepipeline')

    # The Pipeline to Work With
    myPipeline = 'YOUR_PIPELINE_NAME'
    myStage = 'YOUR_STAGE_NAME'
    myAction = 'YOUR_ACTION_NAME'

    # The State of the Pipeline
    state = pipelineClient.get_pipeline_state(name=myPipeline)

    # Get the token value of the latest manual approval step
    myToken = key_search(state, 'token')

    if myToken is None:
        return 'nothing-awaiting-approval'
    else:
        pipelineClient.put_approval_result(pipelineName=myPipeline, stageName=myStage, actionName=myAction,
                                           result={'summary': 'Approved via lambda IoT', 'status': 'Approved'},
                                           token=myToken)

    return 'manual-step-approved'
