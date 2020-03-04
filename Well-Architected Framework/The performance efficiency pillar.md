# The Performance Efficiency Pillar
## Introduction
Nội dung của chapter focus vào việc:

+ Tạo một môi trường test nhanh chóng
+ Scale up & down để đáp ứng nhu cầu của người dùng.
+ Sử dụng các services để tự động hoá quá trình dựng infrastructure
+ Sử dụng container và serverless services một cách tự động.
+ Tự động deploy các ứng dụng phức tạp từ scripts và templates
+ HIểu và tối ưu các operations


## Optimizing Performance for the Core AWS Service
4 phần chính: compute, storage, database và networking.
Nhiệm vụ chính: tune, launch & administrate những tools guips ta quản lý ứng dụng. 

### Compute
#### 1. EC2 Instance Types
Config càng tốt, hiệu quả càng tốt. Cần cân nhắc xem đặt config các `configuration variables` như thế nào cho hợp lý: ECUs, vCPUs, Memory, INstance Storage, EBS-Optimized, ....

#### 2. Auto Scaling
- Scaling out (Scaling horizontally): Thêm resources, chạy song song với resources hiện có. (1 instance không đủ thì thêm 2, 3 instances nữa chạy song song cùng). Lấy 1 snapshot của EBS volume đã được attach vào instances đang chạy, sau đó tạo private EC2 AMI. 
- Auto Scaling sẽ tự động thêm/ tắt instances để phù hợp với nhu cầu. 
- Có thể dùng `launch configuration` để xđ loại instance mà ta muốn thêm.

NOTE: Lệnh cheat để tăng CPU -> Auto Scaling: `while true; do true; done`

#### 3. Serverless Workload
Container tool (Docker) hoặc Lambda: Vừa nhẹ + khởi động, tạo nhanh hơn là full server.

+ Amazone ECS: Nhanh, gọn, nhẹ, chạy trên 1 instance, dễ auto.
+ Lambda functions: Chạy code nhanh

Lựa chọn: 

+ EC2 instaces: Các web app phức tạp. Cần monitoring + tracking chi tiết.
+ ECS: Các app muốn sacle dễ, tự động. Microservices deployments, testing environtment
+ Lambda function: Nhận data từ backend database. Parse data stream, processing transactions.

### Storage
Các loại storage đã biết: EBS (cần quan tâm tới IOPS, latency, throughput settings), S3 & Glacier, EFS. 

#### 1. RAID-Optimized EBS Volumes
RAID: Redundant Array of Independent Disk. 

+ RAID 0: Data bị phân mảnh, lưu trên nhiều hơn 1 device -> bypass a single disk's access limitations. Tăng được IO performance. => Performance
+ RAID 1: Data được nhân bản trên nhiều volumes. => Reliable. 

#### 2. S3 Cross-Region Replication
+ Replication bucket cho phép ta giảm tối đa latency khi người dùng truy cập tại nhiều vị trí khác nhau trên thế giới.
+ Ta có thể config để sync cả bucket hoặc chỉ các objects với prefix.
+ Có thể config để sync với bucket ở region khác, hoặc ở 1 tài khoản khác.

#### 3. S3 Transfer Acceleration
Đây là service cho phép tăng tốc độ transfer large files giữa local PCs và S3 buckets. Ta cần bật tính năng này lên = CLI command.

#### 4. CloudFront and S3 Origins
Ta có thể biến S3 thành hosting file, media, .. Sau đó dùng CloudFront để tối ưu.
### Database
Cần cân nhắc xem nên self-hosted hay dùng service của AWS?

Basic configuration choices:

+ Chọn RDS instance type
+ Tối ưu db dựa vào design schemas, indexes, views
+ Config option groups
+ Config parameter groups.

Dùng của aws sẽ tối ưu hơn, vì đảm bảo đc cho mình các công việc về Consistency, Availability, Partion, Latency, Dủability, Scalability, ....
### Network Optimization and Load Balancing
Focus vào: Geolocation + latency-based routing của Route53 + CloudFront, VPC endpoints, AWS Direct Connects.

+ EC2 instance types cũng có thể ảnh hưởng tới network.
+ Load Balancing: 1 phần mềm để phản hồi lại các incoming requests. Có nhiệm vụ phân tải về các con instances sao cho hợp lý. 
	+ Application Load Balancer: HTTP and HTTPS - layer 7 (application layer)
	+ Network Load Balancer: TCP traffic - Layer 4 (Transpot layer), thường đc dùng cho ECS và CloudFormation.

## Infrastructure Automation
Vì ta sẽ phải dùng đi dùng lại nhiều lần, nên ta nên ốp scripts vào để tăng tính automate + dễ quản lý
### CloudFormation
+ Nhận 2 formats là JSON và YAML
+ Dễ tạo template để import/ export, mỗi môi trường 1 file profile

Cách cách tạo template:

+ Làm trên web, drag & drop
+ Dùng sample template
+ Viết bằng tay sau đó upload template lên 

=> Tạo ra 1 *stack*, nhóm các resources có trong template.
### Third-Party Automation Solution
Sử dụng bash script hoặc dùng các tools khác như Puppet, Chef, Ansible. (AWS OpsWork)
### Continuous Integration and Continuous Deployment
#### AWS CodeCommit
Giống Github, tuy nhiên đc integrated với AWS environment, có thể dùng IAM để set quyền
#### AWS CodeBuild
Là CI, khi push code lên thì chạy test environment :v
#### AWS COdeDeploy
CD - Build server & push app.

Ec2 instances đc quản lý trong 1 `deployment groups` - đc control bằng 1 agent.

#### AWS CodePipeline
Tự động quản lý các phần của CI/CD process.

Khi có push code lên CodeCommit (hoặc Github) thì push code mới đó qua CodeBuild, build chạy test sau đó deploy qua CodeDeploy.
## Reviewing and Optimizing Infrastructure Configurations
+ Quan sát sự thay đổi trong resources config = AWS Config
+ Theo dõi các thông báo mới từ AWS để cập nhật sự thay đổi trong các services (hoặc khi có service mới)
+ Theo dõi performance + avaibility của app qua CloudWatch
+ Test performance + availability để tìm ra vấn đề.

### Load Testing
Giả lập môi trường để xem hệ thống xử lý với workload ntn.

+ Tạo môi trường test = CloudFront/ ECS
+ Fake reqeust từ nhiều geographical origin
+ Setup CloudWatch để theo dõi.


### Visualization
+ Setup SNS để gửi thông báo
+ Vào CloudWatch DashBoard để xem biểu đồ.
+ Dùng widgets để custom combination metrics.
## Optimizing Data Operations
Kiến trúc có thể nhanh nhưng ta cần config để optimize khi transfer 1 lượng lớn data qua weak connection.

Cần tối ưu: Data caching, sharding, compression, decopling.
### Caching
Đối vs những object được request thường xuyên, nên cache lại. Có thể cache trên Memory, sau đó set TTL để expire/ update data đó.

#### Amazon ElastiCache
1 cluster bao gồm nhiều nodes. Số lượng nodes phụ thuộc vào số lượng nhu cầu. Mỗi node là 1 `compute instance`, build từ EC2 instance type mà mình chọn.

Sử dụng 1 trong 2 loại engines: Memcached hoặc Redis.

+ Memcached: Đơn giản, dễ config và deploy, có khả năng scale, run faster. Tuy nhiên chỉ read/write được object blobs - key-value data. Không flexible.
+ Redis: support nhiều loại data types hơn. Data có thể nằm trên disk => có thể recovery. 

Khi tạo xong, ta lấy cluster endpoint ốp vào trong application config.

#### Other Caching Solutions
RDS Replicas, CloudFront

### Partitioning/Sharding
Nếu chỉ có 1 RDS instances thì sẽ khó handle khi có nhiều requests. Shading chia nhỏ db thành nhiều phần (**shard**). Mỗi shard sẽ chứa 1 meta information. Khi data được thêm vào, nó sẽ đc check để nên lưu vào trong shard nào.

### Compression
Nén data lại -> reduce size of data -> Vận chuyển qua network sẽ đơn giản, nhanh hơn.

Đối với data trên disk có thể dùng Disk compression

Static files thì có thể dùng CloudFront

Nếu dữ liệu quá nhiều, muốn đưa lên AWS thì có thể dùng *Snowball* để vận chuyển.
## Summary




















