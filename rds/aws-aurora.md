# Amazon Aurora

Amazon Aurora is a fully managed, MySQL-compatible, relational database engine that combines the performance and reliability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. It delivers up to five times the performance of MySQL without requiring changes to most of your existing applications that use MySQL databases

Cluster endpoint: A cluster endpoint for an Aurora DB cluster that connects to the current primary DB instance for that DB cluster. This endpoint is the only one that can perform write operations such as DDL statements. Because of this, the cluster endpoint is the one that you connect to when you first set up a cluster or when your cluster only contains a single DB instance.
Each Aurora DB cluster has one cluster endpoint and one primary DB instance.
Reader endpoint: A reader endpoint for an Aurora DB cluster connects to one of the available Aurora Replicas for that DB cluster. Each Aurora DB cluster has one reader endpoint. If there is more than one Aurora Replica, the reader endpoint directs each connection request to one of the Aurora Replicas.
The reader endpoint provides load-balancing support for read-only connections to the DB cluster. Use the reader endpoint for read operations, such as queries. You can't use the reader endpoint for write operations.

A **DB cluster parameter group** acts as a container for engine configuration values that are applied to every DB instance in an Aurora database cluster.

A **DB parameter group** acts as a container for engine configuration values that are applied to one or more database instances. Database parameter groups apply to database instances in both Amazon RDS and Aurora. These configuration settings apply to properties that can vary among the database instances within an Aurora cluster, such as the sizes for memory buffers.


Step to detect slow queries:
* Create DB parameter group
* Change config to show slow queries
* Apply this db parameter group to Reader instance and reboot.

To meet your connectivity and workload requirements, Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas provisioned for an Aurora database cluster using single-master replication. Aurora Auto Scaling is available for both Aurora MySQL and Aurora PostgreSQL. Aurora Auto Scaling enables your Aurora database cluster to handle sudden increases in connectivity or workload. When the connectivity or workload decreases, Aurora Auto Scaling removes unnecessary Aurora Replicas so that you don't pay for unused provisioned database instances.

RDS support we add "replica auto scaling" with condition (for CPU or traffic) => Auto scale
