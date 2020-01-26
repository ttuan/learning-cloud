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

You manage hardware resource by instance type/ hardware profile we select.
Consider: Compute power, memory & storage space.

#### Instance Types

* General purpose: aim to provide a balance of compute, memory, and network resources. (T* need virtual volumes, M* has it own volume)
* Compute Optimized: For more demanding web servers and high-end machine learning workloads
* Memory Optimized: intensive database, data analysis, and caching operations.
* Accelerated Computing: achieve higher-performing general-purpose graphics
        pro- cessing unit (GPGPU) performance: 3D visualizations and rendering, financial analysis, and computational fluid dynamics.
* Storage Optimized: distributed file systems and heavyweight data processing applications.

#### Configuration
1. Geographic region
- launch an EC2 instance in the region that’s physically closest to the majority of your customers
- costs and even functionality of services and features might vary between regions
2. VPC
3. Tenacy model
The default setting is shared tenancy, where your instance will run as a virtual machine on a physical server that’s concurrently hosting other instances.
Dedicated Host option allows you to actually identify and control the physical server you’ve been assigned to meet more restric- tive licensing or regulatory requirements.

4. Behavior
User data can consist of a few simple commands to install a web server and populate its web root, or it can be a sophisticated script setting the instance up

#### Pricing
 * less than 12 months - pay for each hour your instance is running through the on-demand model.
