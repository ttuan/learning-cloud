# The Security Pillar

## Introduction
+ Confidentiality: Chỉ có người/system nào có quyền mới có thể access vào data. (Thường dùng Encryption & ACLs)
+ Integrity: Tính toàn vẹn của dữ liệu - Không bị mất hoặc bị thay đổi. (Sử dụng cryptographic hashing và logging)
+ Availability: Luôn khả dụng cho những ai cần nó. 


## Identity and Access Management
> AWS credentials are the keys to the kingdom.

First step: Protect them from accidental exposure and unauthorized use

Second step: Ensure that users have only the permissions they need, and no more.

### Protecting AWS Credentials
*principal* (hoặc *identity*): The root user, IAM user, IAM role.

Ta không nên dùng user root mà nên tạo mới 1 IAM user, sau đó add quyền AdminitratorAccess Policy.

Root user nên bật MFA.

Đối với IAM User, ta nên enforce password policy (độ dài pass, ngày expire, không đc dùng lại, ...)

### Fine-Grained Authorization
Concept: **Chỉ cấp đủ quyền**

Default là IAM users/ roles không có quyền gì. Cần add thông qua policies.

1 policy gồm: 

+ Effect: Allow/Deny
+ Action/Operation: Action có thể tác động lên resource
+ Resource: AWS resource mà ta muốn áp dụng cho action bên trên.
+ Condition: điều kiện để áp dụng (vd restric IP nào mới có quyền)

Có 3 loại policy:

+ AWS Managed Policies: do AWS tạo cho common job.
+ Customer Managed Policies: customer tự tạo, attach vào principals, không overwrite lại policy nhưng tạo mới + lưu 5 version gần nhất.
+ Inline Policies: embeded trong 1 IAM principal/group

### Permissions Boundaries

### Roles

### Enforcing Service-Levl Protection

## Detective Controls
### CloudTrail

### CloudWatch Logs

### Searching Logs with Athena

### Auditing Resource Configurations with AWS Config

### Amazon GuardDuty

### Amazon Inspector

## Protecting Network Boundaries
### Network Access Control Lists and Security Groups

### AWS Web Application Firewall

### AWS Shield

## Data Encryption
### Data at Rest

### Data in Transit

## Summary