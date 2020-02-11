# IAM - Identify and Access Management

- Group - Create group with policies.
- Users - Add user to each group created above.

AWS Identity and Access Management (IAM) can be used to:

* Manage IAM Users and their access: You can create Users and assign them individual security credentials (access keys, passwords, and multi-factor authentication devices). You can manage permissions to control which operations a User can perform.

* Manage IAM Roles and their permissions: An IAM Role is similar to a User, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a Role is intended to be assumable by anyone who needs it.

* Manage federated users and their permissions: You can enable identity federation to allow existing users in your enterprise to access the AWS Management Console, to call AWS APIs and to access resources, without the need to create an IAM User for each identity.

# Policies Evaluation Logic
https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids


# Book
## I. Introduction
+ IAM phụ trách việc authentication và authorization
+ IAM identities: user hoặc role. User là có account/pass, có thể đăng nhập console. Còn Role cung cấp temporarily assigned vào 1 app, service, user, group (sẽ có tác dụng trong 1 khoảng thời gian)
+ Identities được kiểm soát bằng các policies - mô tả xem ai sẽ đc access vào đâu, có quyền gì với resource. CÓ 2 loại: identity-based policies và resource-based policies.
## II. IAM Identities
Khi tạo mới tài khoản thì có root account. Tuy nhiên ta k nên dùng thằng root account này vì nó có toàn quyền vs các resource. Sẽ là mục tiêu của các hackers. Ta nên tạo 1 individual account, cấp đủ quyền cho account đó có thể thực hiện các công việc mong muốn.
### 1. IAM Policies
+ IAM policies là documents chỉ định 1 hoặc nhiều actions - qd xem đối tượng sẽ được làm gì đối với AWS resources. Effect thường có 2 giá trị là Allow và Deny.
+ Có 2 loại policies: 1 là AWS managed policies. 2 là Inline Policies (ng dùng tự tạo)
+ Mọi action không đc chỉ định tường minh sẽ đc hiểu là deny. Nếu bị conflict giữa các policies, nó cũng bị biến đổi thành deny.
+ Deny dùng khi user muốn access "gần hết" các resources trong 1 domain.

IAM policies là global, không restricted to any one region.
### 2. User and Root Account
+ K nên dùng tk root.
+ Các bước để secure account
  + Update pasword
  + MFA
  + Tạo/xóa các access keys để quản lý resources.
  + Tạo key pair để authenticate dùng signedURL với CloudFront.
  + Tạo X.509 certificates để encrypt SOAP request.
### 3. Access Keys
+ Provide authentication for programmatic or CLI-based access. Không phải nhập username/password.
+ Nên deactive các key lâu không sử dụng

#### Key Rotation
Sau 1 thời gian, nên thay key 1 lần để đảm bảo an toàn. Vd: 30 ngày.
+ Tạo access key mới cho users. users có thể quản lý các keys của nó.
+ Update application với key mới.
+ Deactive (không xóa) key cũ.
+ Theo dõi để chắc chắn app vẫn bình thường. Có thể dùng lệnh để check xem app có sử dụng key cũ không.
+ Khi chắc chắn rồi thì xóa key cũ đi.

Key rotation có thể đc setting trong Account Settings/ Password Policy => Force rotation.
### 4. Groups
Tạo user thì sẽ an toàn/ hiệu quả hơn. Nhưng về lâu dài, khi user có nhiều quyền + phức tạo thì sẽ khó quản lý.

Tạo Group thì khi muốn thêm/xóa quyền sẽ tiện lợi hơn. 1 user có thể thuộc nhiều group.

Mỗi team tạo 1 group và loại quyền: admin, devlead, frontend-dev.
### 5. Roles
+ Là 1 identity tạm, cho phép user, service có thể access tới account resource.
+ Khi 1 user cần thêm 1 quyền tạm nào đó, ta tọa mới role, assign vào user đó.
+ 1 IAM Role sẽ default expires sau 12h.
+ Có thể cho phép AWS account khác, hoặc user từ federated service khác access vào dùng resource account của mình.
+ Cần chỉ rõ trusted entity mình muốn cho access:
  + AWS Service
  + Another AWS account
  + Web identity (login with Amazon, Cognito, FB, GG)
  + SAML 2.0 Federation.
+ Khi role được asign, AWS add time-limited token sử dụng **AWS Security Token Service**.
+ Require define trusted entify và ít nhất 1 policy.
## III. Authentication Tools
### Amazone Cognito
Provides user administration for your applications

+ User pools: Có thể add user sign-up hoặc sign-in vào application của mình. QD xem user sau khi sign up thì sẽ dùng gì để identity bản thân => Password, 2FA, email verify sẽ bớt cần thiết hơn.
+ Identity pools: Cho phép users từ application tạm thời có quyền control access tới service khác trong AWS account của bạn.
### AWS Managed Microsoft AD
Các service của Microsofft chạy trong VPC connect tới AWS resource ??
Provide Active Directory authentication within a VPC environment
### AWS Single Sign-On
....
### AWS Key Management Service
+ Manage encryption infrastructure.

Fully managed and **centralized control** over your system-wide encryption.
Có connect tới CloudTrail để quản lý các key-related events.
### AWS Secrets Manager
+ Giúp quản lý pass + third party API keys.
+ Giúp quản lý cả việc rotate key.
+ Handle secrets for third-party services or database.
### CloudHSM
HSM là Hardware Security Module. Để chạy các cryptographic operations. Nhằm giảm lượng lớn việc generate, store, manage cryptographic keys.
Cunng manage encryption infrastructure.

Dùng tốt trong các trường hợp:
+ Keys stored in dedicated, third-party validate hardware security module.
+ FIPS 140-2 compliance.
+ Intergration với app dùng Public Key Cryptography Standards.
+ High-performance in-VPC bulk crypto.
