# VPC - Virtual Private Cloud

Amazon VPC lets you provision a logically isolated section of AWS cloud where
you can launch AWS resources in a virtual network. (Networking, IP address
range, subnets, route tables, network gateways, security settings, ...)


Subnet:
- A subnet is a range of IP address in your VPC. A public subnet must be
    connected to the Internet. A private subnet for resources that won't be
    connected to the Internet.

- A public subnet must have an Internet Gateway, so that traffic can access your
    web server.


Internet Gateway
- Allow communication between instances in VPC with and Intenet


purposes:
+ Provide a target in VPC route tables for Internet routable traffic.
+ Perform network address translation (NAT) for instances which have been
    assigned public IPv4 address.


Route Table
- Contain a set of rules - called routes. Used to determine where network
    traffic is directed. Each subnet in VPC must be associated with a route
    table.

If a subnet is associated with a route table, that has a route to the Internet
Gateway, it's known a public subnet.


Create VPC, Subnet, Internet Gateway.
Create route table. Add route 0.0.0.0/0 to connect Internet Gateway. Add subnet
to this route table.
=> Now your subnet is public subnet.
