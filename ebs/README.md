# Amazon Elastic Block Store

Amazon Elastic Block Store (Amazon EBS) provides persistent block level storage volumes for use with Amazon EC2 instances.
Amazon EBS Snapshots are an easy way to backup data stored on an Amazon EBS Volume. If the volume fails, or data is accidentally deleted, the snapshot can be used to create a new volume. Therefore, it is advisable to frequently take a snapshot of important volumes.

You can think EBS like a Disk Drive, you can attach or detach it from our computer.

Each Amazon EBS volume is automatically replicated within its Availability Zone to protect you from component failure, offering high availability and durability. Amazon EBS volumes offer the consistent and low-latency performance needed to run your workloads. With Amazon EBS, you can scale your usage up or down within minutes – all while paying a low price for only what you provision.

You can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. Snapshots are incremental backups, which means that only the blocks on the device that have changed after your most recent snapshot are saved. This minimizes the time required to create the snapshot and saves on storage costs by not duplicating data. Each snapshot contains all of the information needed to restore your data (from the moment when the snapshot was taken) to a new EBS volume.

In future, this snapshot can be used to create a new volume that will have exactly the same contents as when the snapshot was created.

Amazon EBS volumes are network-attached and persist independently from the life of an instance. Amazon EBS volumes are highly available, highly reliable volumes that can be leveraged as an Amazon EC2 instances boot partition or attached to a running Amazon EC2 instance as a standard block device.
For those wanting even more durability, Amazon EBS provides the ability to create point-in-time consistent snapshots of your volumes that are then stored in Amazon Simple Storage Service (Amazon S3) and automatically replicated across multiple Availability Zones.

## Why
* Persistent storage: Volume lifetime is independent of any particular Amazon EC2 instance.
* General purpose: Amazon EBS volumes are raw, unformatted block devices that can be used from any operating system.
* High performance: Amazon EBS volumes are equal to or better than local Amazon EC2 drives.
* High reliability: Amazon EBS volumes have built-in redundancy within an Availability Zone.
* Designed for resiliency: The AFR (Annual Failure Rate) of Amazon EBS is between 0.1% and 1%.
* Variable size: Volume sizes range from 1 GB to 16 TB.
* Easy to use: Amazon EBS volumes can be easily created, attached, backed up, restored, and deleted.

After attach volume to instance, we need to config file system:
```sh
# Create an ext3 file system on the new volume
sudo mkfs -t ext3 /dev/sdf

# Create a directory for mounting the new storage volume
sudo mkdir /mnt/data-store

# Mount volume
sudo mount /dev/sdf /mnt/data-store
# Mount whenever the instance is started
echo "/dev/sdf   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab

# Test
sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"
cat /mnt/data-store/file.txt
```

## Snapshot
- Provide backup of your data on EBS volumes => Stored in Amazon S3
- It capture data, include any data has been locally cached
- AWS recommend: Detach volume => Create snapshot => ReAttach. If EBS is
    root volume: Shutdown => Create snapshot.
- Only used storage blocks are copied to snapshots, so empty blocks do not take any snapshot storage space.


## Book
The EBS Lifecycle Manager can take scheduled snapshots of any EBS volume, regardless of attachment state.

+ Provisioned IOPS SSD: High Input/Output per second - 32k / 4GB-16TB
+ General purpose SSD: 1Gb-16TB / 10k


Easy to create snapshot and encrypt data.

