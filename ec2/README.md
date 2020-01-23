# EC2 - Elastic Compute Cloud

When you want to down size of EC2:
create snapshot -> tạo disk từ snapshot đó -> Create new VM và attach disk đó vào nếu VM mới khác region

A Bastion host (also known as a Jump Box) is a computer on a network specifically designed and configured to withstand attacks. The bastion generally hosts a single application, for example a proxy server, and all other services are removed or limited to reduce potential threats to the computer.
Security can be further improved by limiting the range of IP Addresses that are allowed to connect to the Bastion host. The best way to do this is to open access only when required, and to remove access when not required. To assist with this, the AWS CLI can be used to grant and revoke security access.

### The Stopinator

The Stopinator is a simple script that turns off Amazon EC2 instances. It can be triggered by cron (Linux) or a Scheduled Task (Windows) and if it finds instances that have a specific tag, it either stops or terminates them.

Schedule the Stopinator to stop machines each evening, to save money.
Mark instances that you want to keep running, then have the Stopinator stop only unknown instances (but don’t terminate them – they might be important!).
Have another script that turns on the instances in the morning.
Set different actions for weekdays and weekends.
Use another tag to identify how many hours you want an instance to run, which is ideal for instances you just want to use for an experiments. Schedule the Stopinator to run hourly and configure it to terminate instances that run longer than the indicated number of hours.

An elastic IP address will not change. A public IP address attached to an instance will change if the instance is stopped, as would happen when changing the instance type

An EC2 instance can access the Internet from a private subnet provided it uses a NAT gateway or NAT instance. No need to stay in public subnet to access the internet
