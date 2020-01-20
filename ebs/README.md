# Amazon Elastic Block Store

Amazon Elastic Block Store (Amazon EBS) provides persistent block level storage volumes for use with Amazon EC2 instances.
Amazon EBS Snapshots are an easy way to backup data stored on an Amazon EBS Volume. If the volume fails, or data is accidentally deleted, the snapshot can be used to create a new volume. Therefore, it is advisable to frequently take a snapshot of important volumes.

You can think EBS like a Disk Drive, you can attach or detach it from our computer.

Each Amazon EBS volume is automatically replicated within its Availability Zone to protect you from component failure, offering high availability and durability. Amazon EBS volumes offer the consistent and low-latency performance needed to run your workloads. With Amazon EBS, you can scale your usage up or down within minutes – all while paying a low price for only what you provision.

You can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved. This minimizes the time required to create the snapshot and saves on storage costs by not duplicating data. Each snapshot contains all of the information needed to restore your data (from the moment when the snapshot was taken) to a new EBS volume.

In future, this snapshot can be used to create a new volume that will have exactly the same contents as when the snapshot was created.
