# S3 - Simple Storage Service

Amazon S3 is object storage built to store and retrieve any amount of data from anywhere on the Internet. It’s a simple storage service that offers an extremely durable, highly available, and infinitely scalable data storage infrastructure at very low costs.

- We can host a static website with s3, just only need `index.html` and `error.html` page.

```
# aws cli command to get bucket name from ec2 console

# Determine Region
AZ=`curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/`
REGION=${AZ::-1}

# Retrieve Amazon S3 bucket name starting with wordpress-*
BUCKET=`aws s3api list-buckets --query "Buckets[?starts_with(Name, 'wordpress-')].Name | [0]" --output text`
```

## Bucket policies
You can control access to data stored in Amazon Simple Storage Service (Amazon S3) by using AWS Identity and Access Management (IAM) policies, bucket policies, or access control lists (ACLs). As a general rule, AWS recommends using user (IAM) policies and bucket policies to control access to Amazon S3 resources, such as buckets and objects.

There are 2 ways to set policies: `Using IAM` and `Using Bucket Policies`

+ IAM Policies: Attach to users, groups or roles to control access to AWS resources.
+ S3 Bucket Policies: Attached to S3 buckets and specify the action a principal can perform on a particular bucket.


Use IAM policies when:
+ If you need to control access to AWS services other than S3 => Centrally
    manage all permissions in IAM instead of managing them between IAM vs S3
+ You have numerous S3 buckets, each with different permissions requirements =>
    Use IAM instead of define large number of S3 bucket policies.

Use S3 bucket policies when:
+ Want simple way to grant cross-account access to your S3 environment, without
    using IAM roles.
+ IAM policies bump up against the size limit (2kb for users, 5kb for groups and
    10kb for roles). S3 bucket policies up to 20kb.

=> Choose based on your prefer, or answer this questions:

+ What can this user do in AWS? => Use IAM.
+ Who can access this S3 Bucket? => Use S3 bucket policies

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3001
```

A more secure option for granting the application access to Amazon S3 resources is to use an instance profile. An instance profile is a container for a single IAM role. Instance profiles are used for this lab because an EC2 instance cannot be assigned a role directly. However, it can be assigned an instance profile that contains a role.

To create the bucket policy, you need to collect additional information for use in the policy. You need the S3 bucket ARN, the AROA ID, and the AWS account information.

To get bucket ARN, AROA ID, AWS information, we use this command: `aws sts get-caller-identity`

```
{
    "Account": "768262736917",
    "UserId": "AROA3FYAHBQKQJ74IGXEA:i-0c82125b50b74d816",
    "Arn": "arn:aws:sts::768262736917:assumed-role/qls-11124143-71406e5bdab7f9e-InstanceIamRoleS3List-15KM2UM3TD8G9/i-0c82125b50b74d816"
}
```
Go to page: https://awspolicygen.s3.amazonaws.com/policygen.html to generate policy & put to permission/bucket policies.

## Cross-region replication
Cross-region replication (CRR) enables automatic, asynchronous copying of objects across buckets in different AWS Regions.
* Comply with compliance requirements: Cross-region replication allows you to replicate data between distant AWS Regions to satisfy these requirements.
* Minimize latency: User in 2 different location can access object copies which is closer
* Increase operational efficiency: Maintain object copies in closer region.
* Maintain object copies under different ownership

#### Policies
 Cross-Region Replication policies are used to determine which objects in a bucket are replicated. You can replicate an entire bucket, a specific folder within a bucket, or any objects with a specified tab. However, objects that already exist in the bucket before replication is enabled will NOT be replicated.

#### Replication

Bucket/Management/Replication

S3-Cross-Region-Replication-Policy sample
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:ListBucket",
                "s3:ReplicateObject",
                "s3:ReplicateDelete",
                "s3:ReplicateTags",
                "s3:GetObjectVersionTagging"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

This is because only new files uploaded to the source bucket after replication is enabled will be replicated to the destination bucket.

we can config which files will be replicate by using prefix (for folder) and tag
(with both key, value) for files.

To protect against malicious intent and accidental deletion, object deletions that occur in a source bucket are not replicated to the destination bucket.
