## AWS CloudFormation/CodePipeline Example

This project uses CloudFormation to spin up a CICD pipeline for Java applications
using CodeBuild, CodeDeploy, CodePipeline, and an EC2 instance.

## Launching the Stack

1. Before launching the stack, create a fork of this [sample java application](https://github.com/ebracho/spring-petclinic). It contains specifications
on how CodeBuild and CodeDeploy should build and deploy the app.

2. Launch the CloudFormation stack by clicking this button:
[![Launch Stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=cloudformation-codepipeline-example&templateURL=https://s3-us-west-2.amazonaws.com/codepipeline-blog/codepipeline-cfn.yml)

3. Fill in the parameters and follow the prompts to complete the launch. For the
GitHub user/repo/branch provide your GitHub username and the master branch of the
fork you created in step 1. If you don't have a GitHub OAuth token, you can generate
one [here](https://github.com/settings/tokens).

4. Watch and wait while CloudFormation provisions all of the resources required
this stack. The process should take roughly 5 minutes.

![CloudFormation Outputs](https://s3-us-west-2.amazonaws.com/codepipeline-blog/cfn-outputs.png)

5. When the stack is complete, retrieve the CodePipeline url from the output
tab and navigate to it. A new revision will have triggered and should be making
its way down the pipeline.

![CodePipeline pre-approval](https://s3-us-west-2.amazonaws.com/codepipeline-blog/code-pipeline-pre-approval.png)

6. After the revision builds, click "Approve" on the approval gate to deploy it to the EC2 server

![CodePipeline post-deployment](https://s3-us-west-2.amazonaws.com/codepipeline-blog/code-pipeline-post-deployment.png)

6. When the deployment completes, retrieve the EC2 instance public DNS name
from the output tab of the CloudFormation stack. Then navigate to <ec2-public-dns-name>/petclinic.

![Petclinic application](https://s3-us-west-2.amazonaws.com/codepipeline-blog/petclinic-application.png)

## Approving a Build  
  
See put-approval-result directory for three ways to approve a manual approval step in a Code Pipeline.  
The first way can be ran via Python 2.7 anywhere `basic.py`.  
`viaAlexa.py` returns a result that is configured for Alexa.  
`viaIoT.py` is meant to be utilized in a Lambda function triggered by an IoT Button.  
