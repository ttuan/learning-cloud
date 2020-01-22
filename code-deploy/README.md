# AWS CodeDeploy

AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, or serverless Lambda functions.

## Why
* Rapidly release new features.
* Update AWS Lambda function versions.
* Avoid downtime during application deployment.
* Handle the complexity of updating your applications, without many of the risks associated with error-prone manual deployments.


## How
Install `codedeploy-agent` on your ec2

AWS CodeDeploy uses the `appspec.yml` file to:

* Map the source files in your application revision to their destinations on the target Amazon EC2 instance.
* Specify custom permissions for deployed files.
* Specify scripts to be run on the target Amazon EC2 instance during the deployment.

The AppSpec file must be named appspec.yml. It must be placed in the root directory of the application's source code.
The AppSpec file is unique to AWS CodeDeploy. It defines the deployment actions you want AWS CodeDeploy to execute. You bundle your deployable content and the AppSpec file into an archive file, and then upload it to an Amazon S3 bucket or a GitHub repository.

Create your CodeDeploy Application
`aws deploy create-application --application-name WordPress_App`
codedeploybucket2806

create s3 bucket and push your code to it
`aws deploy push --application-name WordPress_App --description "This is a revision for the application WordPress_App" --ignore-hidden-files --s3-location s3://BUCKET/WordPressApp.zip --source .`

Crete deployment group
In an EC2/On-Premises deployment, a deployment group is a set of individual instances targeted for a deployment. A deployment group contains individually tagged instances, Amazon EC2 instances in Amazon EC2 Auto Scaling groups, or both. In an AWS Lambda deployment, a deployment group defines a set of AWS CodeDeploy configurations for future serverless Lambda deployment to the group.
`aws deploy create-deployment-group --application-name WordPress_App --deployment-config-name CodeDeployDefault.AllAtOnce --deployment-group-name WordPress_DG --ec2-tag-filters Key=Name,Value=CodeDeploy,Type=KEY_AND_VALUE --service-role-arn arn:aws:iam::055282355277:role/codedeploy-service-role`


Create deployment
`aws deploy create-deployment --application-name WordPress_App --s3-location bucket=codedeploybucket2806,key=WordPressApp.zip,bundleType=zip --deployment-group-name WordPress_DG  --description "This is a revision for the application WordPress_App"`

After update code, use this command to redeploy
`aws deploy push --application-name WordPress_App --s3-location s3://BUCKET/WordPressApp.zip --ignore-hidden-files`
Go to codedeploy revisions tab and create deployment => Config and deploy (you can do it by using aws-cli)
