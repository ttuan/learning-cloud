# Elastic Load Balancing

An Amazon Elastic Load Balancer (Amazon ELB) is a service that automatically distributes incoming application traffic across multiple Amazon EC2 instances.

Elastic Load Balancing detects unhealthy instances within a pool and automatically reroutes traffic to healthy instances until the unhealthy instances have been restored.
The load balancer sends a health check request to each registered target every HealthCheckIntervalSeconds seconds, using the specified port, protocol, and ping path. It waits for the target to respond within the response timeout period. If the health checks exceed the threshold for consecutive failed responses, the load balancer takes the target out of service. When the health checks exceed the threshold for consecutive successful responses, the load balancer puts the target back in service.


Create ELB, config VPC, AZ, Routing (healthy checking path), threshold, ...
Regist Target Group, assign instance into target group.

Network Load Balancers, cross-zone load balancing is disabled by default. After you create a Network Load Balancer, you can enable or disable cross-zone load balancing at any time.
Cross-zone load balancing distributes traffic evenly across all targets in the Availability Zones enabled for the load balancer.

If all of your Amazon EC2 instances in one Availability Zone are unhealthy, and you have set up Amazon EC2 instances in multiple Availability Zones, Elastic Load Balancing will route traffic to your healthy Amazon EC2 instances in those other zones.

Elastic Load Balancing automatically scales its request-handling capacity to meet the demands of application traffic. Additionally, Elastic Load Balancing offers integration with Auto Scaling to ensure that you have back-end capacity to meet varying levels of traffic levels without requiring manual intervention.

Elastic Load Balancing works with Amazon Virtual Private Cloud (VPC) to provide robust networking and security features. You can create an internal (non-Internet facing) load balancer to route traffic using private IP addresses within your virtual network. You can implement a multi-tiered architecture using internal and Internet-facing load balancers to route traffic between application tiers. With this multi-tier architecture, your application infrastructure can use private IP addresses and security groups, allowing you to expose only the Internet-facing tier with public IP addresses.
