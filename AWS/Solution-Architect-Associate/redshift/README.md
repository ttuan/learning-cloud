# Amazon Redshift

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools.
Amazon Redshift delivers fast query and I/O performance for virtually any size dataset by using columnar storage technology and parallelizing and distributing queries across multiple nodes.

An Amazon Redshift data warehouse is a collection of computing resources called nodes. This collection of nodes is called a cluster. When you provision a cluster, you specify the type and the number of nodes that will make up the cluster. The node type determines the storage size, memory, CPU, and price of each node in the cluster


## Scalability

If your storage and performance needs change after you initially provision your cluster, you can always scale the cluster in or out by adding or removing nodes, scale the cluster up or down by specifying a different node type, or you can do both. Resizing the cluster in either way involves minimal downtime. Resizing replaces the old cluster at the end of the resize operation. When you submit a resize request, the source cluster remains in read-only mode until the resize operation is complete.

## Parallel Processing
Amazon Redshift distributes workload to each node in a cluster and processes work in parallel, allowing processing speed to scale in addition to storage.

## Columnar Storage
Columnar storage for database tables is an important factor in optimizing analytic query performance because it drastically reduces the overall disk I/O requirements and reduces the amount of data you need to load from disk.

## Compression
Compression is a column-level operation that reduces the size of data when it is stored. Compression conserves storage space and reduces the size of data that is read from storage, which reduces the amount of disk I/O and therefore improves query performance.

## Snapshots as Backups
Snapshots are point-in-time backups of a cluster. You can create snapshots automatically or manually. Amazon Redshift stores these snapshots internally in Amazon S3 using an encrypted Secure Sockets Layer (SSL) connection.



Import data from files:

The data files are being loaded in parallel from Amazon S3. This is the most efficient way to load data into Amazon Redshift since the load process is distributed across multiple slices across all available nodes.

When you create a table, you can optionally specify one column as the distribution key. When the table is loaded with data, the rows are distributed to the node slices according to the distribution key. Choosing a good distribution key enables Amazon Redshift to use parallel processing to load data and execute queries efficiently.

The CREATE TABLE command you ran earlier designated the carrier (airline) field as the Distribution Key (DISTKEY). This means the data will be split between the all available slices and nodes, but all data related to a particular carrier will always reside on the same slice. This improves processing speed when performing operations on the carrier field, such as GROUP BY and JOIN operations.

Data in Amazon Redshift is stored as columns. This is faster than storing data as rows, since most queries only require a few columns of data. It also allows Amazon Redshift to compress data within each column.
When data is compressed, information can be retrieved from disk faster. Compression conserves storage space, reduces the amount of disk I/O and therefore improves query performance.
