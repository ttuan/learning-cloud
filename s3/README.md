# S3 - Simple Storage Service

Amazon S3 is object storage built to store and retrieve any amount of data from anywhere on the Internet. It’s a simple storage service that offers an extremely durable, highly available, and infinitely scalable data storage infrastructure at very low costs.


* Maintaining backup archives, log files, and disaster recovery images
* Running analytics on big data at rest
* Hosting static website


Unlimited object storage, just only limit 100 buckets/ account

Object Storage: flat, không chứa folder/file. Mình chỉ dùng prefix/ delimiter để
cho nó hiển thị giống kiểu thư mục cho dễ nhìn thôi.
+ Global unique key
+ Metadata (Access control, file system, tags, size, created date)
+ Data (file)


* Tên mỗi bucket là global unique. Do url của object có thể không bao gồm region.
* Một single object không thể lớn hơn 5TB. Mỗi lần uploads thì không được quá
    5GB. Nếu object > 100MB thì **nên** dùng Multipart Upload, còn với object
    lớn hơn 5GB thì **phải** dùng. Multipart UPload girm loss bằng cách chia nhỏ
    file.
* Nếu dùng CLI hoặc high-level API, Multipart UPload được tự động thêm vào. Còn
    ở low-level API, cần custom nhiều hơn.
* Durability: S3 đảm bảo hầu như không bao giờ bị mất dữ liệu vì lỗi phần cứng.
    Nó copy dât tới ít nhất 3 AZs để giúp dữ liệu có thể backup được.
* Eventually consistent data: S3 use "Read After Write". Tức là với write mới
    thì sẽ đọc đc luôn. còn update thì sẽ mất tầm 2s bị delay.
* Presigned URLs: Cho phép tạo ra 1 url tạm, có thể xem được object trong 1
    khoảng thời gian. Mặc định là 1 giờ.


Encryption:

1. SSE: Server side ở đây hiểu là sẽ được encrypt ở trên S3.

+ SSE-S3: S3 dùng luôn key của nó để mã hóa / giải mã
+ SSE-KMS: Dùng KMS để tạo mã.sau đó nén file. Có thể dùng full audit trail để
    tracking key đã sử dụng.
+ SSE-C: Customer Provided Keys: Sử dụng chính key của mình cho việc encrypt.


2. CSE: CLient side
File được encrypt rồi mới chuyển lên S3. Có thể sử dụng CMK(KMS) hoặc Client
side master key.

Log: Vì có quá nhiều event nên S3 không auto lưu lại log. Nếu bạn bật lên, cần
chọn bucket để lưu log. Trong log sẽ có: IP, bucket name, action, time, status.

S3 Class:

+ S3 Standard - Durability: 99.99999999 - Concurent facility fault tolerance: 2 - Availability: 99.99
+ S3 Standard-IA - Durability: 99.99999999 - Concurent facility fault tolerance: 2 - Availability: 99.9
+ S3 One zone-IA - Durability: 99.999999 - Concurent facility fault tolerance: 1 - Availability: 99.5
+ Reduced REdundancy - Durability: 99.99 - Concurent facility fault tolerance: 1 - Availability: 99.99

S3 One Zone-IA và Reduced Redundancy không resilent lắm, vì nó chỉ backup dữ liệu sang 1 concurent facility fault tolerance.

Lifecycle:
+ Do dữ liệu tạo version nhiều quá thì nó rác. Nên cần có cơ chế để chuyển nó
    đi. THường thì sẽ được move sang 1 gói khác. Mình có thể config lifecycle
    rule để sau 30 ngày thì chuyển sang gói One Zone IA, sau 90 ngày chuyển sang
    Glacier, ... sau 365 ngày thì xóa. Không chuyển trực tiếp từ Standard sang
    Reduced Redundancy được.
+ Nên dùng prefix khi apply lifecycle rules.


Security:
+ ACL: Không recommend
+ S3 Policy: Control access tới S3 từ nhiều accounts.
+ IAM Policy: Control mỗi user/role access nhiều resources, trong đó có S3.


S3 and Galicer Select

+ Nếu truy cập bt, sẽ mất nhiều bước để mở được cái file mình muốn -> Tốn phí.
    Dùng S3 Select sạng SQL-like để truy vấn file cho nhanh hơn.


Glacier
+ Gần giống 1 class của S3
+ Max 40TB, của S3 bt là 5TB/1 object.
+ encrypt by default
+ Nhận key IDS được gen bởi máy, S3 dạng "human readable"
+ Giá rẻ
+ Mất nhiều thời gian để access data (hàng giờ). Nếu muốn nhanh thì cần dùng
    Expecdited

=> Chỉ được dùng để lưu các thông tin long-term, unussual and infrequent
circumstatnces.

"archive" ~= object, "vaults" ~= bucket

Amazone Elastic File System:
+ Shareable file
+ Access được từ VPC, mount được vào instance EC2.
+ Low=latency, and durable file shared multiple instances.


Storage Gateway:
Provide 1 applicance để local devices có thể connect vào.
Lưu trữ dât giống S3 hoặc EBS.

AWS Snowball
Với dữ liệu lớn, upload mất nhiều thời gian, AWS gửi 1 thiết bị vật lý tới, mình
truyền data vào đó, sau đó copy dữ liệu vào thiết bị rồi gửi lại AWS.





- We can host a static website with s3, just only need `index.html` and `error.html` page.

```
# aws cli command to get bucket name from ec2 console

# Determine Region
AZ=`curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/`
REGION=${AZ::-1}

# Retrieve Amazon S3 bucket name starting with wordpress-*
BUCKET=`aws s3api list-buckets --query "Buckets[?starts_with(Name, 'wordpress-')].Name | [0]" --output text`
```

## Bucket policies
You can control access to data stored in Amazon Simple Storage Service (Amazon S3) by using AWS Identity and Access Management (IAM) policies, bucket policies, or access control lists (ACLs). As a general rule, AWS recommends using user (IAM) policies and bucket policies to control access to Amazon S3 resources, such as buckets and objects.

There are 2 ways to set policies: `Using IAM` and `Using Bucket Policies`

+ IAM Policies: Attach to users, groups or roles to control access to AWS resources.
+ S3 Bucket Policies: Attached to S3 buckets and specify the action a principal can perform on a particular bucket.


Use IAM policies when:
+ If you need to control access to AWS services other than S3 => Centrally
    manage all permissions in IAM instead of managing them between IAM vs S3
+ You have numerous S3 buckets, each with different permissions requirements =>
    Use IAM instead of define large number of S3 bucket policies.

Use S3 bucket policies when:
+ Want simple way to grant cross-account access to your S3 environment, without
    using IAM roles.
+ IAM policies bump up against the size limit (2kb for users, 5kb for groups and
    10kb for roles). S3 bucket policies up to 20kb.

=> Choose based on your prefer, or answer this questions:

+ What can this user do in AWS? => Use IAM.
+ Who can access this S3 Bucket? => Use S3 bucket policies

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3001
```

A more secure option for granting the application access to Amazon S3 resources is to use an instance profile. An instance profile is a container for a single IAM role. Instance profiles are used for this lab because an EC2 instance cannot be assigned a role directly. However, it can be assigned an instance profile that contains a role.

To create the bucket policy, you need to collect additional information for use in the policy. You need the S3 bucket ARN, the AROA ID, and the AWS account information.

To get bucket ARN, AROA ID, AWS information, we use this command: `aws sts get-caller-identity`

```
{
    "Account": "768262736917",
    "UserId": "AROA3FYAHBQKQJ74IGXEA:i-0c82125b50b74d816",
    "Arn": "arn:aws:sts::768262736917:assumed-role/qls-11124143-71406e5bdab7f9e-InstanceIamRoleS3List-15KM2UM3TD8G9/i-0c82125b50b74d816"
}
```
Go to page: https://awspolicygen.s3.amazonaws.com/policygen.html to generate policy & put to permission/bucket policies.

## Cross-region replication
Cross-region replication (CRR) enables automatic, asynchronous copying of objects across buckets in different AWS Regions.
* Comply with compliance requirements: Cross-region replication allows you to replicate data between distant AWS Regions to satisfy these requirements.
* Minimize latency: User in 2 different location can access object copies which is closer
* Increase operational efficiency: Maintain object copies in closer region.
* Maintain object copies under different ownership

#### Policies
 Cross-Region Replication policies are used to determine which objects in a bucket are replicated. You can replicate an entire bucket, a specific folder within a bucket, or any objects with a specified tab. However, objects that already exist in the bucket before replication is enabled will NOT be replicated.

#### Replication

Bucket/Management/Replication

S3-Cross-Region-Replication-Policy sample
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:ListBucket",
                "s3:ReplicateObject",
                "s3:ReplicateDelete",
                "s3:ReplicateTags",
                "s3:GetObjectVersionTagging"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

This is because only new files uploaded to the source bucket after replication is enabled will be replicated to the destination bucket.

we can config which files will be replicate by using prefix (for folder) and tag
(with both key, value) for files.

To protect against malicious intent and accidental deletion, object deletions that occur in a source bucket are not replicated to the destination bucket.

S3 uses a read-after-write consistency model for new objects, so once you upload an object to S3, it’s immediately available.
S3 cross-region replication transfers objects between different buckets. Transfer acceleration uses a CloudFront edge location to speed up transfers between S3 and the Internet.
With SSE-C you provide your own keys for Amazon to use to decrypt and encrypt your data. AWS doesn’t persistently store the keys.
Applying encryption to an unencrypted object will create a new, encrypted version of that object. Previous versions remain unencrypted.
