# Auto Scale

- Auto Scale is a way to set "cloud temperature". Use policies to "set the thermostat", and Under the hood, AutoScaling controls the heat by adding and subtracting EC2 resources on an as-need basis in order to maintain the "temperature" (capacity). An Auto Scaling policy consists of:
  - A `launch configuration` that defines the servers that are created in response to increased demand.
  - An `Auto Scaling group` that defines when to use a launch configuration to create new server instances and in wich Availability Zone and load balancer context they should be created.

- AS assumes a set of homogeneous servers. That is, AS does not know that Server A is a 64 bit extra-large instance and more capable than a 32-bit small instance. This is a core tenet of cloud computing: scale horizontally using a fleet of fungible resources; individual resource are secondary to the fleet itself.


When you launch a server manually, you provide parameters such as: Amazon
Machine Image (AMI), which instance type, and which security group in ==
**launch configuration** - define what kind of instance to launch.

Auto Scale group tell system what to do with an instance after it is launched. -
define Zone, which LB to connect, Min and Max number of instances to run at any
time. -> It uses **scaling policies**
We should use CloudWatch Alarm to trigger.

Scaling takes time - Check condition (2min) - CloudWatch check(1min) -
AutoScaling (1min) - Boosting server - LB poll server and pass requests to it.

```bash
# ElasticLoadBalancer, qls-10958-ElasticL-NWYNVTDJ55X9
# AMIId, ami-08d489468314a58df
# KeyName, qwikLABS-L2322-10958927
# AvailabilityZone, us-west-2a
# SecurityGroup, qls-10958927-e2e17bae8c5f634c-Ec2SecurityGroup-1SKMZRKPMBDQJ

# Create configuration
aws autoscaling create-launch-configuration --image-id ami-08d489468314a58df --instance-type t2.micro --key-name qwikLABS-L2322-10958927 --security-groups qls-10958927-e2e17bae8c5f634c-Ec2SecurityGroup-1SKMZRKPMBDQJ --user-data file:///home/ec2-user/as-bootstrap.sh --launch-configuration-name lab-lc

# AutoScaling Group
aws autoscaling create-auto-scaling-group --auto-scaling-group-name lab-as-group --availability-zones us-west-2a --launch-configuration-name lab-lc --load-balancer-names qls-10958-ElasticL-NWYNVTDJ55X9 --max-size 4 --min-size 1

```

Auto Scaling instances run without name => Use Tags

```bash
aws autoscaling create-or-update-tags --tags "ResourceId=lab-as-group, ResourceType=auto-scaling-group, Key=Name, Value=AS-Web-Server, PropagateAtLaunch=true"
```

Load Balancer - Instances tabs, chi co instance dc nhan len thoi, k co instance goc?


SNS

```bash
aws autoscaling describe-auto-scaling-notification-types

aws autoscaling put-notification-configuration --auto-scaling-group-name lab-as-group --topic-arn arn:aws:sns:us-west-2:844522662412:lab-as-topic --notification-types autoscaling:EC2_INSTANCE_LAUNCH autoscaling:EC2_INSTANCE_TERMINATE
```
Add CloudWatch for High CPU and Low CPU (select EC2 - CPUUltility - config alarm SNS, notification, ...)

Scaling:

```bash
# Scaling Up
aws autoscaling put-scaling-policy --policy-name lab-scale-up-policy --auto-scaling-group-name lab-as-group --scaling-adjustment 1 --adjustment-type ChangeInCapacity --cooldown 300 --query 'PolicyARN' --output text

# Scaling Down
aws autoscaling put-scaling-policy --policy-name lab-scale-down-policy --auto-scaling-group-name lab-as-group --scaling-adjustment -1 --adjustment-type ChangeInCapacity --cooldown 300 --query 'PolicyARN' --output text
```

To test scaling up, run a background process to copy, zip and unzip ~1G of nothing (/dev/zero) for 10-20 mins :v

The instances were terminated in launch order => the oldest instances were terminated first
