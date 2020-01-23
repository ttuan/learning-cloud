# AWS CloudFormation

AWS CloudFormation gives developers and systems administrators an easy way to create and manage a collection of related AWS resources, provisioning and updating them in an orderly and predictable fashion.

Type attribute: `AWS::ProductIdentifier::ResourceType`. For example:
`AWS::S3::Bucket`

Delete stack in CloudFormation can delete resource (for example: delete
bucket in s3). So in yaml file, use option `    DeletionPolicy: Retain` to
keep resource


When modify resources, just consider:
* How does the update affect the resource itself? (As you have seen, changing
    the instance type requires that the instance be stopped and restarted)
* Is the change mutable or immutable? In the case of mutable changes, AWS
    CloudFormation will use the Update or Modify type APIs for the underlying
    resources. For immutable property changes, AWS CloudFormation will create
    new resources with the updated properties and then link them to the stack
    before deleting the old resources (for example: changing the AMI on an
    EC2)

FYI: The cfn-hup helper is a daemon that detects changes in resource metadata and runs user-specified actions when a change is detected. This allows you to make configuration updates on your running Amazon EC2 instances through the UpdateStack API action.
/etc/cfn/cfn-hup.conf: stores the name of the stack and the AWS credentials that the cfn-hup daemon targets.
/etc/cfn/hooks.d/cfn-auto-reloader.conf: The cfn-hup daemon parses and loads each file in this [hooks.d/] directory. The user actions that the cfn-hup daemon calls periodically are defined in the hooks.d/*.conf configuration file.

## Book
Almost everything in CloudFormation is case sensitive
