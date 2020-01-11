# S3 - Simple Storage Service

- We can host a static website with s3, just only need `index.html` and `error.html` page.

```
# aws cli command to get bucket name from ec2 console

# Determine Region
AZ=`curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/`
REGION=${AZ::-1}

# Retrieve Amazon S3 bucket name starting with wordpress-*
BUCKET=`aws s3api list-buckets --query "Buckets[?starts_with(Name, 'wordpress-')].Name | [0]" --output text`
```
