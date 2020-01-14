# CloudWatch

CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources. Using simple rules that you can set up in a couple of minutes, you can easily route each type of event to one or more targets, including AWS Lambda functions with less overhead and greater efficiency. You can think of CloudWatch Events as the central nervous system for your AWS environment. It is wired in to each of the supported services, and becomes aware of operational changes as they happen. Then, driven by your rules, it activates functions and sends messages to respond to the environment.

We can create `Event/Rules` with mapping service events (like EC2 instances
starting) with other action (ex: lambda function)
