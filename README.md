# Step Functions poc
Proof of Concept for Step Functions from AWS

## Use-Case

Use step functions to demonstrate an orchestration workflow for integration testing

### Problem statement

Conduct an integration test for validating a docker image

* Create an Autoscaling group of ECS Optimized AMI (ECS/Docker installed by default)
* Create an ECS Cluster
* Create ECS Task Definition for an Nginx image
* Create an ALB/Target group for Load balancing the container
* Curl http://{alb_address} and check the HTTP return code is 200

### Solution

#### Base Artifacts

* Create a Cloudformation template to create ASG/ECS Cluster/ALB/FeaultTargetGroup
* Create a Lambda function that launches the Cloudformation template
* Create a lambda function that checks the execution state for Cloudformation stack
* Create a Lambda function that does the following
  * Create an ECS Task Definition with Nginx image
  * Create an ECS Service with the TD
  * Add Load balancing for the service using the TG
* Create a Lambda function that takes an URL and reports the response code
* Create a Lambda function that destroys the CFT
* Create a Lambda function for status reporting

#### Step Functions Design

* In the initial state, create the Cloudformation stack. Make sure the stack reports success only after ECS agent and Docker are up
* In the next state, check the status of stack and loop using an appropriate approach until stack enters "CREATE_COMPLETE"
* In the next state, use Lambda Task to create TD/service
* In the next state, loop until successful 200 response code or timeout after X min
* Upon success or timeout, destroy the stack
* Send status of all activities
* End the workflow
