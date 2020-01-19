# Relation Database Service

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easy to set up, operate, and scale a relational database in the cloud.

Support: MySQL, SQL Server, Oracle or PostgreSQL

You will reconfigure a Drupal Open Source Content Management System (CMS) to use Amazon RDS for MySQL as the backend database with a multi-Availability Zone (AZ) deployment model.

### Why
* Pre-configured Parametters: pre-configured with a sensible set of parameters.
* Monitoring & Metrics: view compute/memory/storage/IO activiy and DB Instance Connections.
* Automated Backups: Turned on by default. Enables point-in-time recovery. (from 5 minutes to 35 days)
* DB Snapshots: user-initiated backups of DB instance. We can create new DB
    instance from a DB Snapshots.
* Provisioned IOPDS (Input/Output Opreations Per Second) - SQL Server can set max to 7000 IOPS
* Push-Button Scaling: Scale up/down easy
* Automatic HOst Replacement: AUto replace the instance powering deploymen tin
    event of a hardware failure.
* Replication: Multi-AZ
* Isolation and Security



Standard storage vs Provisioned IOPS storage.
Provisioned IOPS is a storage option => deliver fast, predictable, consistent
I/O performance, optimized for I/O intentsive, transactional db workloads.


## How to setup
+ Create private subnet (Subnet is created in VPC)
+ Create security group for database (in VPC)
+ Create subnet group in RDS.
+ Create RDS database.

=> Get Endpoint and connect.
