# CloudWatch

CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources. Using simple rules that you can set up in a couple of minutes, you can easily route each type of event to one or more targets, including AWS Lambda functions with less overhead and greater efficiency. You can think of CloudWatch Events as the central nervous system for your AWS environment. It is wired in to each of the supported services, and becomes aware of operational changes as they happen. Then, driven by your rules, it activates functions and sends messages to respond to the environment.

We can create `Event/Rules` with mapping service events (like EC2 instances starting) with other action (ex: lambda function)

We can config to view networking log - Log in VPC.

We can discovery log in CloudWatch:

+ Successful HTTP calls were made from each web server, 404 requests ,...
+ Which IP addresses of last IAM user logged in, what action did user take?
+ Top 20 IP address in Access logs
+ Which IP address access to 3306, 22, ...


====
Livestream video

- MediaLive push alerts -> CloudWatch Events -> Use SNS as a target -> SNS: Push
    message to topic.

- Create and save dashboard


====
Add VPC log (EC2, VPC, ...) log to CloudWatch. Write a lambda function to add this logs to Elastic Search => Use Kibana to view this log.

We can use this way to detect `Brute force attacks`, `SSH attacks` or other attacks

# Book
## Introduction
Cloudwatch tracks log for AWS resource và applications.

1. Tracking performance: Từ đồ thị, số liệu => khi nào cần scale up or out
2. Detect application problems: Xem log, nếu chưa exception/warning/404,.. -> fix bug sớm.
3. Detect security problems: Track hđ của user giúp giảm risk và phát triển tính bảo mật.
4. Log events: Có đầy đủ thông tin về các action tác động lên resource.
5. Mainating an Inventory of AWS resource: Check được resource được config ntn.

CloudTrail: Giữ detailed logs cho mọi hđ read & write xuất hiện trong AWS resources.

CloudWatch: thu thập numeric perfomance metrics từ các AWS resources hoặc non-resource (server đã chạy). Cho phép search logs dễ hơn, cung cấp cảnh báo, thực hiện action nếu vượt ngưỡng threshold.

AWS Config: tracks xem AWS resource được config ntn, thay đổi ntn theo thời gian.

## CloudTrail
**Event** là 1 record của 1 hành động mà tác động lên AWS resource. CloudTrail logs read/write actions qua các thông tin: Action, resource, region, ai làm và khi nào.

CloudTrail log log both API & non-API actions (thực hiện trên console).

Chia làm 2 loại event: *management events* và *data events*

### Management Events
Bao gồm các hoạt động thực thi chính tới resource. - control plane operations.

Nhóm thành *read-only* và *write-only* events. Write-only events là các API operations mà modify hoặc có thể modify resources. Read-only events là các API operations đọc resources nhưng không tạo thay đổi gì.
### Data Events
Track 2 loại data plane operations có xu hướng là high-volume: S3 object-level activity và Lambda function executions.

Ex: GetObject - readonly event, DeleteObject/PutObject - write-only event.
### Event History
Đây là 1 tính năng, có thể truy cập từ side menu trong CloudTrail.

CloudTrail log 90 ngày cho management events và lưu chúng để có thể xem, search, download. Trong này không bao gồm data events (do quá nhiều :v)

Tạo History riêng biệt cho mỗi region.
### Trails
Hỗ trợ tạo lưu log bao lâu, service/actions nào, hoặc lưu cả data events => Hãy tạo `trail`.

Config này để tạo JSON records với events và chuyển tới S3 bucket.

+ eventTime: Date time of action.
+ userIdentity: id lquan tới việc thực thi: IAM role/user, ARN, IAM username.
+ eventSource: Global endpoint của service mà action thực thi.
+ eventName: tên của API operation.
+ awsRegion: nơi resource đc đặt.
+ sourceIPAddress: IP của requester.

Tạo trail có thể config cho 1 hoặc nhiều regions. Max 5 trails cho 1 regions.

### Log File Integrity Validation
Đảm bảo tính toàn vẹn của logs file, đảm bảo là không cso log files nào bị sửa hoặc bị xoá sau khi được tạo.

Dùng hash file để check xem file có bị modify hay không. Mỗi giờ, nó sẽ tạo 1 `digest file`, chứa tất cả các hash mã hoá của các file logs được chuyển tới trong giờ vừa qua. File này được đặt cùng bucket với log nhưng chia trong folder khác, đc set quyền để không bị xoá. Mỗi digest file này chứa cả hash của digest file trước đó.

Có thể sử dụng AWS CLI command để check validate của logs file từ trail arn và start time.

Log + digest files được encrypt = SSE-S3. Có thể chọn SSE-KMS.
## CloudWatch
Các resources tự động gửi metrics tới cho CloudWatch. Ta cũng có thể config để gửi custom metrics tới CloudWatch từ application và server có sẵn.

Từ các logs được gửi, ta có thể tạo ra các custom metrics, vd như số lượng lỗi đc log từ app.
### CloudWatch Metrics
Metrics được gom lại thành các `namespaces`. Vd: AWS/EC2, AWS/S3,..

Dùng namespace để tránh confuse với những metric tên gần giống nhau. Metrics chỉ tồn tại trên region nơi nó đc tạo.

Metrics được tạo từ các `data-points` -> Các điểm dự liệu mà sẽ đc dùng để vẽ biểu đồ.

Metric đc unique từ: namespace, name và dimension. dimemsion có thể là 1 cặp name-value (InstanceID: xxxxx).

#### Basic & Detailed Monitoring
* Basic monitoring: Gửi metrics tới CloudWatch mỗi 5 phút. EBS sử dụng basic monitoring cho gp2 volumes. Mỗi phút nó thu thập dữ liệu 1 lần. Nhưng gửi ntn lại tuỳ vào hypervisor.

* Detailed monitoring: Gửi metrics mỗi phút 1 lần.

#### Regular and High-resolution Metrics
Thực ra là timestamp resolution.

* Regular resolution metrics: Có timestamp resolution từ 1 phút trở lên.

* High-resolution metrics: Custom metrics với timestamp resolution nhỏ hơn 1 phút.

#### Expiration
CloudWatch sẽ chuyển từ high-resolution về thành regular resolution.

+ Sau 3h, các data point chuyển về 1-minute resolution
+ Sau 15 ngày, 5 data points gộp lại, chuyển thành 5-minutes resolution.
+ Sau 63 ngày, 12 data point gộp lại, chuyển thành 1-hour resolution.
+ Sau 15 tháng thì metrics sẽ bị xoá.

### Graphing Metrics
Xem các metrics bằng cách vẽ các data-point theo thời gian.

**Statistics**: Sum, Minimum, Maximum, Average, Sample count, Percentile.

Để vẽ đc 1 metric cần có: Metric, Statistic và Period.

Muốn vẽ 1 graph metric as is, ta chỉ cần chọn period = metric's resolution. Ta có thể chọn time range là độ dài của trục thời gian.


### Metric Math
Dùng khi ta muốn combine nhiều metrics lại thành 1 time series. (vd số error rates).

Các hàm: AVG, MAX, MIN, STDDEV, SUM
Thường sẽ phải dùng thêm hàm METRICS() để chuyển dữ liệu. vì dữ liệu của các hàm statistic thường trả về dữ liệu vô hướng, k dùng để vẽ được.
## CloudWatch Logs
Feature để thu thập logs từ resource/ non-resources, lưu trữ, search, và tách custom metrics. Thường đc dùng để lấy CLoudTrail logs, thu thập application logs từ instance, logging Route 53 DNS queries.
### Log Streams and Log Groups
Log events: Các records của hoạt động, đc lưu lại bởi application/resource. Cần có timestamp và event message.

Same source log events sẽ đc lưu vào trong **log stream**. Ta có thể xoá manual log stream, nhưng k thể xoá log events. Ta không set được thời gian để xoá logs stream, phải set dựa trên log group.

Log streams đc tổ chức trong các **log groups**. Nên set thời gian để xoá những log này đi, 1 ngày -> 10 năm hoặc lưu vĩnh viễn. CŨng có thể export để đẩy lên S3.
### Metric Filters
Dùng để tách data từ logs trong log group để tạo ra CloudWatch metrics. Ví dụ có thể filter 404 để tạo ra metrics HTTP404Errors.

Có thể tách số, string, dùng regex, ...

Metrics filters khi được apply vào log group thì có thể tạo metric, nhưng nó không check lại dữ liệu cũ, trước khi metric filter đc ốp vào.
### CloudWatch Agent
Agent nằm trên EC2 instances, cho phép tạo metric custom, thu thập logs, thông số trên EC2 để gửi về CloudWatch.

CloudWatch Log Agent chỉ thu thập log, còn thằng này thì thu thập đc nhiều thông tin hơn.
### Sending CloudTrail Logs to CloudWatch Logs
Có thể gửi CloudTrail logs tới CloudWatch Logs log stream.

Vì CloudTrail không có search log, nên nếu đẩy sang cloudwatch log thì sẽ có thể search + extract đc metrics.

Ta cần chỉ cụ thể log group và IAM role sẽ sử dụng. Có thể mất 1 khoảng thời gian để log từ CloudTrail pass qua CloudWatch Logs. CloudTrail không chuyển log > 256KB.
## CloudWatch Alarms
Quan sát metric để thực hiện actions dựa trên 1 điều kiện nào đó. (>= threshold chẳng hạn). Action có thể là: send mail, reboot instances, auto scale, ...

### Data Point to Monitor
Metric's resolution khác với **periods** của alarm (mặc dù cả 2 cái này đều có đơn vị thời gian). Ví dụ: metric resolution là 5 mins. Còn period là 15 phút. Thì sau 15 phút, CloudWatch sẽ lấy ra được 3 metrics data points. sau đó nó tính trung bình, để tạo ra 1 **data point to monitor**.

Tức là: Data point to monitor là 1 giá trị trung bình của các data points trên 1 khoảng periods.

Ta nên set periods >= resolution của metric. Vì nếu nhỏ hơn, nó sẽ vẽ k đúng.
### Threshold
Là giá trị của Data point to monitor cần đạt hoặc vượt ngưỡng để khiến somethign went wrong.
### Alarm States
**Data points to Alarm** là số lần data point to monitor vượt ngưỡng threshold liên tục. Vd: periods là 5 mins. data point to alarm là 3. Nếu data points to monitor vượt threshold liên tục trong 15 phút thì sẽ có cảnh báo.

+ **ALARM**: Data point to alarm đã bị crossed.
+ **OK**: Data point to alarm chưa vượt ngưỡng.
+ **INSUFFICIENT_DATA**: Chưa thu thập đủ data để check xem data points to alarm đã bị vượt chưa.
### Data Points to Alarm and Evaluation Period
Bình thường thì data point to alarm sẽ cảnh báo nếu vượt ngưỡng n lần liền tục trong 1 khoảng thời gian.

Còn nếu bạn muốn check nếu vượt ngưỡng m lần, nhưng không cần liên tục, thì nên dùng Evaluation period.

set số evaluation period >= data point to alarm

`m out of n alarm`: m là số data point to alarm, còn n là là evaluation periods.
Tức là vượt ngưỡng m lần trong khoảng n alarm thì sẽ báo.

Evaluation period không dài hơn đc 24h.
### Missing Data
Nếu tháo EBS/ stop instances,... sẽ bị mất dữ liệu để thống kê. Nên ta cần config action đối với những missing data đó:

+ **As missing**: Coi như không có period bị mất data, bỏ qua luôn.
+ **Not Breaching**: Coi như data period bị mất không vi phạm vào threshold.
+ **Breaching**: Coi như data của period bị mất đã vị phạm vào threshold.
+ **Ignore**: Bỏ qua period bị mất, tiếp tục đợi đến khi đủ dữ liệu mới alarms.
### Actions
+ SNS: Push notifications tới các subscribers đã subscribe vào topic. Cần có endpoint (email address, queue,...)
+ Auto Scaling: Tạo Auto Scaling policy để add/remove instance.
+ EC2 Action: Stop, terminate, rebott, recover instance. Nó chỉ tồn tại khi metric mình đang theo dõi có dimension chưa InstanceID.
## AWS Config
Track AWS resource được config ntn theo thời gian. Giống như 1 cái time machine vầy. Ngoài track đc resource, nó còn track cả thông tin các resource liên quan.

+ Security: Thông báo khi resource config thay đổi, cảnh báo sớm.
+ Dễ audit reports: Tạo snapshot của các config tại bất cứ thời điểm nào.
+ Trouble shooting: Quan sát config tại thời điểm bị lỗi, xem gợi ý config thiếu/ dễ bị ảnh hưởng tới resource khác.
+ Change managements: Xem mức độ ảnh hưởng nếu mình thay đổi.
### The Configuration Recorder
+ Core của AWS config. Nhờ nó mà ta xem đc resource hiện có, record xem chúng thay đổi ntn.
### Configuration Items
Tạo 1 configuration items cho mỗi resource. Bao gồm: resource type, ARN, đc tạo khi nào, các mối quan hệ vs các resource khác.

Khi resource bị xoá nó cũng track đc.

Items này đc lưu ở AWS Config, và ta không thể xoá bằng tay được. chỉ có thể đợi nó hết hạn là tự xoá.
### Configuration History
Bao gồm nhiều configuration items. Bao gồm detail về các resources, như đc tạo khi nào, đc config ntn, khi nào bị xoá, ...

Mỗi 6h, AWS config chuyển các history file tới S3 bucket. S3 bucket đc coi như **delivery channel**. File đc group bởi resource type. Các file này đã đc đánh dấu dựa trên thời gian, và giữ trong các thư mục dựa vào ngày tạo.

Ta có thể chọn SNS topic như 1 delivery channel để báo khi có thay đổi trong resource.
### Configuration Snapshots
Tập các configuration items tại 1 thời điểm.

Sau 1 khoảng thời gian, AWS Config sẽ tự động chuyển configuration snápshot tới delivery channel. (vd up lên s3 sau 1 ngày chẳng hạn). Thời gian delivery frequency có thể là mỗi giờ, hoặc mỗi 3,6, 12, 24h.
### Monitoring Changes
Mỗi khi có thay đổi trong resource config, AWS config sẽ tạo 1 configuration item mới để lưu lại sự thay đổi trong resource này và các related resources với nó.

Configuration items sẽ default lưu trong 7 năm, thấp nhất là sẽ đc lưu trong 30 ngày. Cái này k áp dụng với configuration history và cònig snapshot file đã chuyển tới S3.

Ta có thể stop configuration recorder bất cứ lúc nào. khi đó sẽ k monitor đc sự thay đổi. nhưng configuration items vẫn sẽ đc lưu.

Có thể theo dõi đc nhiều phần khác trong EC2 instance, vd như apps, CLI, firewall config, windows update, ... Nhưng cần dùng EC2 Systems Manager.

Ta có thể tạo rule để validate config resource. AWS đã cung cấp khá nhiều rule có sẵn, ta có thể chọn tạo thành bộ rule riêng cho resources của mình. Nếu fail sẽ thông báo. Khi active, rule sẽ đc check hàng giờ hoặc sau 3, 6, 12, 24h.


=> Ta nên config CloudWatch và AWS Config trước khi bắt đầu dự án.
CloudWatch track về performance metrics + take action. Thu thập log để search + extract metrics.

CloudTrail giữ record của các activity, sử dụng cho security hoặc auditing.
