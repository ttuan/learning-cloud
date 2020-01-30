# AWS Elastic Beanstalk

Beanstalk is a managed service that abstracts the provisioning of AWS compute and networking infrastructure. You are required to do nothing more than push your application code, and Beanstalk automatically launches and manages all the necessary services in the background.

```sh
# Demo command with eb
eb create --database --vpc.id vpc-06c329321cb51d130 --vpc.dbsubnets subnet-0afd41b2e594f31b8,subnet-0da225c7c8110ec96 --vpc.ec2subnets subnet-0afd41b2e594f31b8,subnet-0da225c7c8110ec96 --vpc.elbsubnets subnet-0d99b9f5c35059ae9,subnet-06226f92e973e9723 --vpc.elbpublic -db.i db.t2.micro -db.engine mysql --elb-type application --service-role aws-elastic-beanstalk-service-role --instance_profile qls-11325344-e3bb73d6d1415d52-AWSBeanstalkEc2Role-1GSDQXYSRU6PF
```

