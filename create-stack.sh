#!/bin/bash

STACK_NAME_PREFIX=codepipeline-test

if [ -f stackid.txt ]; then
  echo "Deleting current stack..."
  aws cloudformation delete-stack --stack-name $STACK_NAME_PREFIX-`cat stackid.txt`
  sleep 3
fi

openssl rand -hex 4 | sed 's/..$//' > stackid.txt

echo "Creating new stack $STACK_NAME_PREFIX-`cat stackid.txt`"

aws cloudformation create-stack \
  --stack-name $STACK_NAME_PREFIX-`cat stackid.txt` \
  --template-body file:////Users//liatrio//work//AWSCodePipeline//code-pipeline-cfn//codepipeline-cfn.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=ApplicationName,ParameterValue=petclinic \
               ParameterKey=GitHubUser,ParameterValue=ebracho \
               ParameterKey=GitHubRepo,ParameterValue=spring-petclinic \
               ParameterKey=GitHubOAuthToken,ParameterValue=$GITHUB_OAUTH_TOKEN \
               ParameterKey=BranchName,ParameterValue=master \
               ParameterKey=InstanceType,ParameterValue=t2.micro \
               ParameterKey=KeyName,ParameterValue=$DEFAULT_KEY_PAIR_NAME \
               ParameterKey=DeploymentNameTag,ParameterValue='tomcat-test'

if [ $? -ne 0 ]; then
  rm stackid.txt
fi
