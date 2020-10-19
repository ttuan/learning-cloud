# Relation Database Service

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easy to set up, operate, and scale a relational database in the cloud.

Support: MySQL, SQL Server, Oracle or PostgreSQL, Aurora, MariaDB

Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ).

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


## Book
#### How to
+ Manage database
+ Protect your data
+ Recover it if it fail


## Relation database
+ Relation database phải có ít nhất 1 table. Column (attribute) và rows
    (records/ tuples). Phải define column name và data type trước khi muốn thêm
    data.
+ Column được order và không thể thay đổi order sau khi tạo bảng.
+ Thường được dùng cho app cần query data và customize cách data được hthi.
+ Qhuan hệ 1-n, bảng 1 được coi là parent table và bảng n được gọi là child
    table.

#### Online Transaction Processing và Online Analytic Processing
+ OLTP:
  + Phù hợp với app cần read & write nhiều.
  + Optimized cho các regular + predictable queries.
  + Có thể store queries thường dùng trong memory để access nhanh hơn.
+ OLAP:
  + Optmized cho các queries phức tạp + data set lớn.
  + Thông thường, người ta thường kết hợp nhiều OLTP với 1 OLAP.
  + Nhiều server có thể share khả năng tính toán để xử lý query phức tạp.


## Amazon Relation Database Service
+ Setting up, backup, high availlability
+ Easy to recovery, scale data.


### Database Engines
+ MySQL (Storage engine: MyISAM + InnoDB), MariaDB (gần giống MySQL), Oracle,
    PostgeSQL (gần giống Oracle, nhưng free), Amazon Aurora (write performance,
    cover được MySQL + PostgreSQL, hỗ trợ migrate từ db cũ, được lưu = mySQL/
    PostgreSQL sang, support only InnoDB) và Microsoft SQL Server.

#### Licensing Considerations
+ License Included: Phí cho DB engine đã bao trong phí RDS instance.
  + Free (MySQL, MariaDB, PostgresSQL).
  + SQL Server, Oracle (SE1, SE2)
+ Bring your own license: Dùng license của mình.
  + Sp: Oracle(EE, SE, SE1, SE2)


#### Database Option Groups
+ Là feature thêm, option cho instance. Nếu dùng sẽ tăng memory, nên ensure nếu
    muốn bật lên.

### Database Instance Classes
+ Giống type của EC2 instance, có thể thay đổi được.

#### 1. Standard: Meet the needs of most database.
#### 2. Memory Optimized: Dùng cho app cần nhiều memory, memory to => cache được
nhiều hơn trên memory => faster query. Là EBS optimized => dedicated bandwidth
for transfer to/from EBS storage.
#### 3. Burst Capable: Dùng cho nonproduction databases. Throughput <= 3200 Mbps
(400 MBps).

### Storage

#### IOPS
+ IOPS càng cao, read/write càng nhanh.
+ IOPS phụ thuộc vào loại storage mà ta chọn.
+ Lượng dữ liệu mà ta cso thể vận chuyển trên mỗi lần I/O phụ thuộc vào **page
    size**. MySQl và MariaDB là 16 KB (tức là 1 lần ghi có thể ghi 16KB vào
    disk). Còn Oracle, PostgreSQL, Microsoft SQL Server có page size là 8KB.

+ IOPS = Throughput / page size
    16 KB = 0.128Mb


#### 1. General-purpose SSD
+ Fast, new volume up to 16TB.
+ 1 GB <=> 3 IOPS. Từ nhu cầu của app, tính được số throughput, từ số throughput + page size, tính ra được số IOPS, từ IOPS tính
    ra được số GB cần thiết để đáp ứng được throughput.
+ Minimum storage volume depend on DB engine. SQL Server Enterprise là 200GB,
    loại khác là 20GB.

+ Volume nhỏ hơn 1 TB có thể temporary burst lên 3k IOPS trong 1 khoảng thời gian:

    Burst duration in seconds = (Credit balance) / [3000 - 3 * (storage in GB)]

Khi instance boot, ta có credit balance = 5,4 triệu IOPS.

#### 2. Provisioned IOPS SSD (io1)
+ Mình tự setting số IOPS mình cần.
+ Tỉ lệ IOPS: storage (GB) ít nhất phải là: 50:1


#### 3. Magnetic Storage
+ Limit 4 TB và 1000 IOPS.

Phân biệt được sự khác nhau giữa Read Replica và Multi AZ.

### Read Replicas
+ Nếu gặp vấn đề với memory, compute, network speed, disk-throughput, ta có thể upgrade db instance (scaling vertically/ scaling up)
+ Biện pháp thứ 2 là scaling horizontally (scaling out), tức là tạo thêm nhiều db instances làm read replicas. Oracle + Microsoft SQL Server không support read replicas. Aurora sp kiểu replica riêng gọi là Aurora Replica.
+ Dùng tốt khi app read nhiều.
+ Dữ liệu được đồng bộ từ con master sang read replicas nên sẽ bị delay 1 tí. => Read replica không phù hợp để recovery nếu gặp sự cố.
+ Chỉ có read-endpoint, đc load balance.
+ Replica và master có thể nằm ở AZ khác nhau, hoặc ở regions khác nhau. Khi master down, có thể đưa thằng replica lên làm master, nhưng có thể bị mất dữ liệu. Do **asynchronous**

### High Availabilty (Mutil AZ)
+ Deploy trên nhiều AZ để đảm bảo an toàn.
+ Có 1 primary db instance ở 1 AZ, và 1 standby db instance ở AZ khác. Khi primary bị outage, sẽ chuyển qua thằng standby sau khoảng 2 phút.

#### Multi AZ với Oracle, MySQL, PostgreSQL, MariaDB, Microsoft SQL Server
+ Muốn multi AZ deployment, tất cả các DB instances phải nằm trong cùng 1 region.
+ Dữ liệu được synchronously replicate từ primary tới standby instance.
+ Standby không phục vụ read traffice. Nếu có lỗi xảy ra, RDS thay DNS record để trỏ từ con primary tới endpoint của con standby. App mình chỉ cần reconnect lại.
+ Nếu dùng MySQL/ MariaDB, ta có thể tạo multi AZ read replica trên các region khác nhau.

#### Multi AZ với Aurora
+ Cluster chưa primary instace có thể chứa cả read replica.
+ Primary + all read replicas share single cluster volume.
+ Khi bị fail, nếu có replica => Đưa replica lên làm primary instance. Nếu k có replica => Tạo 1 primary instance mới.

#### Backup and Recovery
+ Tạo EBS volume snapshot
+ Khi restore từ snapshot, RDS sẽ restore trên 1 instance mới.

##### Automated Snapshots
+ Nên chọn thời gian DB "nhàn rỗi" nhất. vì tạo snapshot sẽ ảnh hưởng tới performance.
+ RDS xoá automated snapshot sau 7 ngày, có thể config từ 1-> 35 ngày.
+ Có thể manual take snapshot.

## Amazon Redshift
+ OLAP database, based on PostgreSQL.
+ Tối ưu hoá cho query data.
+ Compress encoding để giảm size khi lưu vào storage.

### Compute nodes
+ Dense compute node: Store up 326 TB on magnetic storage.
+ Dense storage node: Store up to 2 PB trên fast SSD.

Nếu cluster chứa nhiều compute node, Redshift thêm `leader node` để phụ trách việc giao tiếp giữa các compute nodes.

### Data Distribution Styles
+ Row trong Redshift DB phân tán giữa các node. Việc phân chia dữa liệu phụ thuộc vào distribution style.
	+ EVEN distribution: Leader node chia dữ liệu evenly across compute nodes.
    + KEY distribution: Chia dữ liệu theo value trong 1 column. Columns có cùng value thì sẽ đc lưu trên 1 node.
    + ALL distribution: Every table is distributed to every compute node.

## No-SQL DB
+ Lưu trữ unstructed data.
+ Dùng để query data based on only one attribute.

#### Storing Data
+ Schemaless.
+ Primary key là unique identify an item and provide a value by which to sort items.

#### Querying data
+ Nonrelational DB được tối ưu cho những queries dựa trên primary key.

#### Types ò Nỏnealtional DB
1. Key-value stores
2. Document-oriented stores: Phân tích content của document stored như 1 value và extracts metadata từ nó.
3. Graph database: Phân tích mối quan hệ giữa các attributes trong các items khác nhau => Khám phá ra các mối quan hệ trong unstructed data.

## Dynamo DB
+ Chia nhỏ data ra thành nhiều partition <=> 1 table

#### Partition and Hash Keys
+ Khi tạo table cần chỉ định primary key + data type.
	+ Partition key (hash key) là 1 primary key chỉ chứa 1 value. Vì ta dùng parttion key như là primary key => simple primary key. (email, unique username, ..) - max 2048B.
    + Composite primary key: Tổ hợp của: partition key + sort key.

+ Dynamo DB phân bố items vào các partitions dựa vào primary key. Thằng nào có primary key giống nhau thì cho vào 1 partition, sau đó đc sắp xếp theo sort key. (sort key < 1024B)

+ Nếu có nhiều request vào 1 partition (hot partition), ta nên cố gắng make partition keys as unique as posible.

#### Attributes and Items
+ 1 items có nhiều attributes, mỗi attribute là 1 cặp key-value.
+ Data type: Scala (1 value), Set, Document. (list, map, ...)

### Throughput Capacity
+ Provisioned throughput: Số read/write mỗi giây mà app cần. DynamoDB dựa vào số read capacity units (RCUs) và write capacity units (WCUs) để tính dự trữ partition.
+ Throughput là lượng data được vận chuyển trên 1 đơn vị thời gian.

+ Khi read 1 item từ table:
	+ Strongly consistent: Luôn đọc được dữ liệu up-to-date.
    + Eventually consistent: Có thể trả về dữ liệu cũ, k phải từ write operation mới nhất.

+ Với Strongly consistent: 4 KB item = 1 RCU, 8 KB item = 2 RCU strongly consistent read.
+ Eventually consistent read: 8 KB item = 1 RCU
+ Write: 1 KB = 1 WCU.

#### Auto Scaling
....

#### Reserved Capacity
+ Nếu xd đc trước WCU hoặc RCU, nên chọn thằng này để giảm giá.

### Reading Data
+ Scan: List all items trong 1 table.
+ Query: Trả về item dựa trên value của partition key. Value của partition key ta search phải match chính xác với 1 item. Với sort key thì có thể search dựa vào điều kiện: exact value, greater than, les than, ...

#### Secondary indexes
+ Nếu search kiểu trên thì có vấn đề là phải nhập chính xác partition key. Secondary index giúp mình tìm kiếm bằng 1 attribute chứ k dùng table's primary key.
+ Nó tạo ra 1 base table: projected attributes (attribute mình sẽ lấy ra để search), partition key và sort key.????

##### 1. Global Secondary Index
+ Có thể tạo sau khi tạo bảng.
+ Partition và hash keys có thể khác trong base table.???
+ Item với partitions có same value sẽ lưu ở cùng 1 partition.
+ Read are always eventually consistent.

##### 2. Local Seconday Index
+ Cần tạo cùng lúc với base table.
+ Partition key phải giống với trong base table. Nhưng sort key có thể khác.
+ Read có thẻ là strongly hoặc eventually consistent.
