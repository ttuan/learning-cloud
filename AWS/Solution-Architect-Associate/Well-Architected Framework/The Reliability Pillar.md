# The Reliability Pillar

## Introduction
Reliability là khả năng application tránh được failure và recover nhanh khi bị fail.

Trước khi bắt đầu kiến trúc AWS deployment, bạn nên quyết định "How much reliability bạn thực sự cần". Core term của reliability là **availability** - % thời gian mà application chạy đúng như expect.

Ta sẽ focus vào 3 mục: network, storage, compute.

Có 2 loại fail: 1 là do AWS. 2 là do bugs, security breach, database corruption, ... từ phía application của mình.
## Calculating Availability
Tính toán % thời gian mình muốn app available. Vd: 99% (1 năm sẽ có 3 ngày, 15h, 39p app down), ..
### Availability differences in traditional vs Cloud-Native Applications
#### 1. Traditional Applications
App được viết chạy trên Linux hoặc Window servers. Cần chạy trên EC2 instances. DB dùng self-hosted hoặc RDS.

Nếu bạn có 1 traditional app chạy trên EC2, bật multi-AZ => Availability phụ thuộc vào cả EC2 instance và RDS instance -> *hard dependencies*

**Availaibility = Multiply the availability of those hard dependencies**.

EX: Ec2 = 99.99%, multi AZ RDS = 99.95% => availability = 0.9999 * 0.9995 = 99.94%
Để tăng tính khả dụng, ta có thể sử dụng `redundant components`. Vd dùng nhiều instance EC2 trong ALB.

**Availability = 100% - product of the instance failure rate**
EX: EC2 = 99.99% => Availability = 100% - (0.01% * 0.01%) = 99.99999%

#### 2. Cloud-Native
App đc viết chỉ sử dụng resource của cloud platform. (serverless app, sử dụng store objects trên S3, hoặc sử dụng DynamoDB thay vì realtional database)

=> % availability sẽ cao hơn, linh hoạt hơn khi ta dùng kết hợp: DynamoDB, EC2 ALB, nhiểu regions, ...

#### 3. Building Serverless Applications with Lambda
- Không cần chạy EC2 lieent tục, chỉ khi nào cần hoặc chạy thì mới tính phí.
- Tương tác tốt vs các service khác (S3, CloudWatch, ..) sẽ đc trigger từ các serivce đó
- High avaibility.
### Know Your Limits
AWS vẫn có limit với 1 số dịch vụ. Ta có thể sử dụng Trusted Advisor để xem giới hạn với tk của mình.
### Increasing Availability
+ Dùng nhiều instances nhỏ, thay vì dùng 1 thằng to. Đặt các instance này ở các AZ khác nhau. Nhưng thế này dẫn đến 1 vđ: Nếu 1 instance fail, các instance còn lại sẽ phải chịu traffic của instance fail đó => Ta cần dùng Auto Scale nữa.
+ Nên chọn scale out (add thêm instances) hơn là scale in (upgrade power cho instance) vì scale in sẽ require down time.
## EC2 Auto Scaling
Tránh lỗi và recover nếu có lỗi xảy ra. Tự động thêm instances để đáp ứng với nhu cầu. Nếu có 1 instance fail, AS sẽ tự đổng replace nó bằng 1 instance healthy khác.

AS sử dụng cả `launch configuration` và `launch template` để tự động chạy config. Cả 2 thằng này đều sẽ định nghĩa basic config parameters + scripts để chạy lúc launch time. Launch templates mới hơn và được AWS recommends.
### Launch Configurations
Khi tạo mới instance, ta cần làm rất nhiều việc: Dùng AMI nào, instance type, SSH key pair, security group, instance profile, EBS optimized, user data, ... Launch Configuration tổng hợp các bước này vào 1 document.

Có thể tạo launch configuration cho 1 instance EC2 có sẵn. Auto Scaling sẽ copy settings của instance, ta cũng có thể custom lại.

Launch Configuration **chỉ** được dùng cho Auto Scaling, không thể tạo mới instance với laun configuration này được. Một khi đã tạo, bạn không thể modify launch configuration. Nếu muốn thay đổi gì, ta phải tạo mới 1 launch configuration khác.
### Launch Templates
Về cơ bản thì giống với launch configuration

+ Có thể dùng cho Auto Scaling, nhưng cũng có thể dùng để chạy mới 1 instance
+ Quản lý theo versions. Cho phép thay đổi sau khi tạo. Có thể flip back giữa các version.
+ Có thể copy launch configuration to launch template.
### Auto Scaling Groups
Là 1 nhóm các EC2 instances. Khi tạo AS Group, ta cần chỉ định launch configuration hoặc launch template. Cần chỉ rõ các giá trị sau:
+ Minimum: Số lượng healthy instances không đc nhỏ hơn số minimum.
+ Maximum: Số lượng healthy instances không được vượt quá maximum.
+ Desired capacity (optional). Mặc định sẽ = số minimum. Nếu chỉ định số này, AS sẽ tạo số lượng instance = desired capacity => còn đc gọi với tên khác là *group size*

#### ALB Target Group
Chỉ định 1 ALB target group khi tạo AS group để chỉ định ALB phân bổ traffic vào trong các instances. Khi scale out, instance mới đc tạo, cũng tự đc add vào trong ALB target group.

#### Health Checks Against Application Instances
+ Default là dùng EC2 Health-checks.
+ EC2 locally perform system and instance status checks (tạo metrics gửi lên CloudWatch)
+ Có thể config health check cho ALB target group. (HTTP request)
### Auto Scaling Options
#### Manual scaling
Có thể set lại min/max/desired number sau khi tạo group. AS sẽ tự động điều chỉnh số lượng instances để đáp ứng.

#### Dynamic Scaling Policies
Tự động scale dựa trên thông số CPU, request, ... để scale tự động trước khi hit point. AS generate metrics dựa vào: CPU, request tới target, network bytes in/out.

Dynamic scaling policies hoạt động dựa vào việc quan sát CloudWatch alarm và scaling out khi có alearm.
Có 3 loại sacling policies là: simple, step và target tracking.
##### 1. Simple Scaling Policies
Khi nào metric đạt tới threshold, AS sẽ tự động tăng desired capacity. Tăng bao nhiêu thì tùy thuộc vào `adjustment types` mà mình chọn:

+ ChangeInCapacity: Tăng đúng 1 lượng nhất định (ví dụ mỗi tần tăng lên 2 instances chẳng hạn)
+ ExactCapacity: Tăng lên tới 1 số (Ví dụ nếu vượt quá thì tăng lên đủ 6 instances)
+ PercentChangeInCapacity: Tăng capacity theo % số instance hiện tại. (vd tăng thêm 50% số lượng instance hiện tại).

Sau khi sacle xong, sẽ có 1 cooldown period trước khi policy được check tiếp. trung bình là đợi 300s.

##### 2. Step scaling policies
Nếu nhu cầu của app tăng nhanh quá, simple scaling policies k đáp ứng đủ, ta nên thay bằng step scaling policie: Add thêm instances dựa vào số lượng các metrics vượt threshold.khi CPU trung bình của các instance trong group đạt ngương 50%, ta add thêm 2 instances. Nếu đạt ngưỡng 60%, ta add thêm 4 instances nữa.

+ Tạo CloudWatch alarm
+ Điền step adjustment: Lower bound, upper bound, adjustment type, amount by which to increase the desired capacity.

Sẽ đợi trong khoảng warnup time 300s để instance mới hđ, tính lại trung bình CPU rồi mới tính tiếp.

##### 3. Target tracking policies
Chọn metric và target value. AS sẽ tạo 1 CloudWatch Alarm và 1 sacling policy để giữ số lượng instance sao cho metric gần với target nhất.

Metric được chọn phải là các metric dạng "Thay đổi theo tỷ lệ". Vd: % CPU trung bình của group, request count per taget. (Tổng số request count tới ALB thì không chọn được).

Có scale in - tự xóa instance để đảm bảo giữ được số metric.
##### Scheduled Action
Dùng trong trường hợp ta ó thể dự đoán được load parttern, muốn chắc chắn được là có đủ tài nguyên trước khi demand hít.

Ta cần xđ: min, max, desired capacity value + start date and time.
Có thể đặt repeating load pattern.
## Database Backup and Recovery
### S3
- Chọn Storage classes trừ One Zone - Infrequent Access để có thể lưu object trên nhiều AZ.
- Bật S3 versioning để S3 never overwrites or delete an object mà sẽ gắn 1 delete marker + remove from view.
- Bật cross-region replication để copy sang bucket ở region khác. (Cái này cần bật versioning lên trước)
### Elastic File System
Network File System có thể được share giữa các EC2 instances. EFS filesystem được lưu giữa nheiefu zone trên 1 region.

Do không có versioning nên ta cần phải backup file lên s3 hoặc 1 EFS filesystem khác trên cùng region.
### Elastic Block Storage
Auto replicate volumes giữa các AZ trên 1 region.
Nên tạo các snapshot và lưu trên S3. Ta có thể dùng Data Life Cycle Manager để tự động tạo snapshot sau 1 khoảng thời gian (có thể chọn 12 hoặc 24h). Cần chọn số lượng snashot to retain: up to 1000 snapshots.

Dùng CloudWath logs để thu thập, lưu trữ log từ instance in real time, đề phòng trường hợp EBS bị toang và Auto Scaling xóa mất instance.
### Database Resiliency
+ Nếu tự chạy DB trên instance, cần chạy lệnh backup DB ra 1 file, sau đó lưu trên S3/ Glacier.
+ Nếu sử dụng RDS, nên tạo database instance snapshot. Khi cần thì tạo instance mới từ snapshot đó.
+ Có thể sử dụng multi AZ RDS deplyment để cho primary instance ở 1 zone, standby instance ở 1 zone khác.
+ Sử dụng Aurora với nhiều replicas. Lưu trên 3 ÁZ, up to 15 replicas.
+ DynamoDB lưu trên nhiều ÁZ, nhanh, bảo vệ tốt dữ liệu. Có thể sp replicate table tới regions khác. CÓ thể config point-in-time recovery tới thời điểm bất kì từ 35 ngày trước - 5 phút trước.
## Creating a Resilient Network
### VPC Design Considerations
Chắc chắn lại là mình đã chọn CIDR block cung cấp đủ IP address để asign tới your resources.

Khi tạo subnet, để đủ khoảng trống CIDR để có thể add thêm subnet sau này vì:
+ Khi AWS có thêm AZ mới trên 1 region, ta có thể tạo thêm subnet mới trên AZ mới đó.
+ Chúng ta vẫn cần chia nhỏ app ra thành nhiều subnets để bảo mật hơn.

Trên mỗi subnet cũng nên để trống 1 ít space. Đề phòng nhu cầu tăng, add thêm instances.
### External Connectivity
Phụ thuộc vào mức độ khả dụng network của users dùng khi access vào nó.

Nên chọn Direct Connect: Cần fast and reliable connection to AWS. But make sure your VPC addresses don't overlap with Direct Connect/VPC peering/ VPN connection.
## Designing for Availability
Cần cân nhắ giữa availability, complexity và cost.
### 99 Percent Availability
EC2: app + DB. S3: Backup DB with versioning. Route53 health check.  Direct user to statis page trên S3 nếu healcheck failover.

#### Recovery Process
Nên dùng CloudFormation để tạo nhanh, config SG nhanh, ... và còn có thể chạy thử để test.
### 99.9 Percent Availability
Dùng distributed application design.

Chạy nhiều instances trên nhiền ÁZs, Config ALB, perform health check các instances. Tạo launch template để instance app cho nhanh. Add AutoScaling group, chạy ít nhất 6 instances trên 3 ÁZs.

For DB: dùng multi-AZ RDS deployment. Nếu primary toang, RDS sẽ failover tới secondary instance ở zone khác. Setup automated db snapshots để bật point-in-time recovery -> giảm RPO xuống còn 5 phút.
### 99.99 Percent Availability
Chạy đồng thời appliation trên 2 regions, 1 active region và 1 passive region.  AutoScaling thì đặt instance trên nhiều AZ khác nhau, ensure mỗi zone có thể chịu 50% peak load.

Sử dụng multi-AZ. primary + secondary DB nằm trên cùng 1 region. Nếu dùng MySQL/ MariaDB thì ta có thể tạo multi AZ read replica trên region khác. và đồng bộ data từ region này sang region khác. Delay có thể khoảng 10 phút.

Nếu 1 region bị fail, ta cần:
+ Thay Route53 resource record để redirect users sang ALB ở standbay region.
+ Promote read replica trên passive region để nó thành primary DB instance.
