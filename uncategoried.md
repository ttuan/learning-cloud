1. The Business plan offers access to a support API, but the Developer plan does not.
2. Customers are responsible for managing the network configuration of EC2 instances. AWS is responsible for the physical network infrastructure.

# Core AWS Service
## Cloud Computing and AWS

The technology that lies at the core of all cloud operations is virtualization.
Virtualization split to small units: Physical Server, Compute Resource, Storage, Hypervisor, VMs.

+ We can control project time (on/off server), the usage, bills (on-demand)
+ Scalable (auto add resources), elastic (reduce capacity when demand drops), cheaper, effective deployment.

#### AWS Cloud
+ Compute: replicating the traditional role of local physical servers for the cloud - Auto Scaling, Load Balancing, EC2, Lambda, Elastic Beanstalk.
+ Networking: Connectivity, Access Control, Enhanced Remote connections. - VPC,
    Direct Connect, Route 53, CloudFront
+ Storage: Storage file, backup. - S3, Glacier, EBS, Storage Gateway
+ Database: Relation, noSQL, Caching - RDS, DynamoDB
+ Application Management: Monitoring, auditing, configuring AWS account service and running resource. - CloudWatch, CloudFormation, CloudTrail, Config
+ Security & Identity: Authentication and Authorization - IAM, KMS, Directory Service
+ Application integration - SNS, SWF, SQS, API Gateway

17 regions - Each region contains multiple Availability Zones.

3 ways to control AWS: Console, AWS CLI, AWS SDK

#### The AWS Shared Responsibility Model
- The customer responsible for: **What's IN the Cloud** - Customer data, User Application, Access Management, Operating System, Network, Access Configuration, Data Encryption.
- AWS Responsible for: **The Cloud Itself** - Hardware and Network Maintenance, AWS Global Infrastructure, Managed Service

#### The AWS Service Level Agreement
By “guarantee,” AWS doesn’t mean that service disruptions or security breaches will never occur.
The important thing to remember is that it’s not if things will fail but when. - May fail but it will notice us.



#### AWS Plans
- Basic: Free, can access customer services, documentation, white papers and support forum.
- Developer: $29/month, adds access for one account holder to a Cloud Support associate along with limited general guidance and “system impaired” response.
- Business: $100/month (and up), eliver faster guaranteed response times to unlimited users for help with “impaired” systems, personal guidance and troubleshoot- ing, and a support API.
- Enterprise: At least $15,000/month, cover all of the other features, plus direct access to AWS solutions architects for operational and design reviews, your own technical account manager, and something called a support concierge.



## EC2 and EBS

## S3 and Glacier Storage

## VPC

## Database

## Authentication and Authorization - IAM

## CloudTrail, CloudWatch and AWS Config

## Domain Name System (DNS) and Network Routing - Route 53 and CloudFront

# The Well-Architeched Framework

## The Reliability Pillar

## The Performance Efficiency Pillar

## The Security Pillar

## The Cost Optimization Pillar

## The Operation Excellence Pillar
