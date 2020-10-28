# Amazon Elastic IP Address

When EC2 Instance restarted, the IP Address will be changed. To keep:

Public IP: try to use an Elastic Ip, then you will not have this problem anymore. You can allocate an new one to your instance directly on AWS Console or programmatically. But if your are using an autoscaling-group you will have to do it on your user-data or cloud-init process.

Private IP: Unfortunately you cannot fix a private Ip address to an instance. The only way is to use DNS and in that case a private DNS zone for you VPC (https://docs.aws.amazon.com/fr_fr/vpc/latest/userguide/vpc-dns.html). No need to buy a domain in that case.

I would also recommend to use DNS on the first case with maybe a domain you have rather than using an IP address

Create private DNS zone for VPC like hostname ~= service name in docker-compose.
This container pings to other container by using service name, not internal
container ip :D
