# IAM
[https://cloud.google.com/iam/docs/overview](https://cloud.google.com/iam/docs/overview)

## How IAM works
> Control who (identity) has what access (role) for which resource

Permissions thường được group lại vào thành *roles*, sau đó *roles* được gán cho authenticated users.

IAM policy chỉ ra: Roles nào được gắn với members nào. Và policy này được gắn vào resource. Khi muốn thao tác gì đó vào resource, IAM check polices của resources để biết xem action đó có được phép không.

![](https://cloud.google.com/iam/img/iam-overview-basics.svg)

## Concepts related to identity
Ngoài 4 loại: Google Account, Service Account, Google group, Cloud Identity domain, ta còn có thêm `allAuthenticatedUsers` -> Chỉ tất cả những người dùng internet đã đăng nhập GG Account và `allUsers` - tất cả user trên Internet.

## Concepts related to access management
- **Permissions** determine what operations are allowed on a resource.
- A **role** is a collection of permissions. You cannot grant a permission to the user directly. Instead, you grant them a role.
	- Basic roles: Owner, Editor, Viewer (Role chung, chứa nhiều quyền, k nên assign trên prd)
	- Predefined roles: Roles được định nghĩa sẵn, giới hạn quyền hơn Basic roles. **automatic updated**
	- Custom roles: Người dùng tự tạo roles, chỉ định các permissions có trong role. **not be updated automatically** (khi có quyền mới cập nhật trên GCP, quyền đó không được tự động thêm vào bên custom roles)

- You can grant roles to users by creating an **IAM policy**, which is a collection of statements that define who has what type of access

- Nên bố trí theo Resource hierarchy recommends để dễ dàng tạo IAM policies cho các cấp.

Command: `gcloud iam roles describe`

## Roles

### Basic roles
- Còn gọi là `primitive roles`
- Owner chứa quyền của Editor, Editor chứa quyền của Viewer.
	- `roles/viewer` - Chỉ view
	- `roles/editor` - Viewer permissions + changing existing resources.
	- `roles/owner` - Editor permissions + **manage roles and permissions** + **setup billing**

### Predefined roles
- Give granular access to specific Google Cloud resources and prevent unwanted access to other resources.


Services | Roles Detail | roles |
---|---|---|
Compute | - **Admin**: Full control of all Compute Engine resources. (\*) <br> - **Instance Admin (beta)**: Permissions to create, modify, and delete virtual machine instances. This includes permissions to create, modify, and delete disks, and also to configure Shielded VM settings. (\*) <br> Example, if your company has someone who manages groups of virtual machine instances but does not manage network or security settings and does not manage instances that run as service accounts, you can grant this role on the organization, folder, or project that contains the instances, or you can grant it on individual instances.<br> - **Network Admin**: Permissions to create, modify, and delete networking resources, except for firewall rules and SSL certificates. The network admin role allows read-only access to firewall rules, SSL certificates, and instances (to view their ephemeral IP addresses). The network admin role does not allow a user to create, start, stop, or delete instances. <br> Example, if your company has a security team that manages firewalls and SSL certificates and a networking team that manages the rest of the networking resources, then grant the networking team's group the networkAdmin role. <br> <br> (*): If the user will be managing virtual machine instances that are configured to run as a service account, you must also grant the **roles/iam.serviceAccountUser** role. | roles/compute.admin<br> roles/compute.instanceAdmin <br> roles/compute.networkAdmin |
Storage | - **Admin**: Grants full control of objects and buckets. When applied to an **individual bucket**, control applies **only to** the specified bucket and objects within the bucket. <br> <br>- **Object Admin**: Grants full control of objects, including listing, creating, viewing, and deleting objects.    <br> <br>    - **Object Creator**: Allows users to create objects. Does not give permission to view, delete, or overwrite objects. <br> <br> - **Object Viewer**: Grants access to view objects and their metadata, excluding ACLs. Can also list the objects in a bucket. <br> <br> Storage Legacy roles - **Legacy Object Reader**: Can get a object but can not list | roles/storage.admin <br> roles/storage.objectAdmin <br> roles/storage.objectCreator <br> roles/storage.objectViewer <br> <br> roles/storage.legacyObjectReader|
App Engine | - **Admin**: Read/Write/Modify access to all application configuration and settings. <br>  <span style="color: red">Application owner/administrator - On-call engineer - Sys Admin</span>  <br> <br> - **Service Admin**: <br> + Read-only access to all application configuration and settings. <br>+ Write access to service-level and version-level settings, including traffic configuration. <br> + Cannot deploy versions of apps, see separation of duties below for details. <br> <span style="color: red">Release engineer - DevOps - On-call engineer - Sys Admin</span> <br><br> - **Deployer**: <br> + Read-only access to all application configuration and settings. <br> + Write access only to deploy and create a new version. <br> + Delete old versions that are not serving traffic. <br> + Cannot modify an existing version, nor change traffic configuration. <br> <span style="color: red">Deployment account - Release engineer</span> <br> <br> - **Viewer**: Read-only access to all application configuration and settings. <br> <span style="color: red">User needing visibility into application, but not to modify it. <br> Audit job checking App Engine configuration for policy compliance.</span> <br> <br> - **Code Viewer**: Read-only access to all application configuration, settings, and deployed source code. <br> <span style="color: red">User needing visibility into application and its source code, but not to modify it. <br> DevOps user needing to diagnose production issues.</span> | roles/appengine.appAdmin <br> roles/appengine.serviceAdmin <br> roles/appengine.deployer <br> roles/appengine.appViewer <br> roles/appengine.codeViewer ([Reference](https://cloud.google.com/appengine/docs/standard/java/roles)) |
+ Spanner
+ BigQuery

### Custom roles
- Custom roles enable you to enforce the principle of least privilege => Tự tạo ra roles của riêng mình, assign permissions hợp lý.
- Khi tạo mới 1 custom role, bắt buộc phải chọn Organization hoặc Project cho nó.
- Permission luôn có cú pháp: <span style="color: red">service.resource.verb</span> (ví dụ: `compute.instances.list`). Permission thường mapping 1:1 với REST API. Ví dụ `topic.publish()` cần permission `pubsub.topics.publish`
- Để có thể tạo custom role cần quyền `iam.roles.create` do đó **owner** của **Project** hay **Organization** đều có quyền này
- Users who are not **owners**, including organization administrators, **must be assigned** either the <span style="color: red">Organization Role Administrator role</span> (**roles/iam.organizationRoleAdmin**) or the <span style="color: red">IAM Role Administrator role</span> (**roles/iam.roleAdmin**). The IAM Security Reviewer role (**roles/iam.securityReviewer**) enables the ability to view custom roles but not administer them.
	- `roles/iam.organizationRoleAdmin` - Control all custom roles trong organization.
	- `roles/iam.roleAdmin` - Control all custom roles cho project.

- Ta không thể change role IDs, nên đặt role ids cẩn thận. Có thể xoá custom role, nhưng k thể tạo mới custom role với cùng ID, có thể phải đợi tới 37 ngày mới xoá xong =)). Trong 7 ngày đầu tiên, ta có thể khôi phục (undelete) 1 custom role đã xoá.
- **Read-Modify-Write**: Để tránh trường hợp 2 người cùng edit 1 roles, GG dùng `etag` property để phân biệt. [Read more](https://cloud.google.com/iam/docs/creating-custom-roles#read-modify-write)

## References
- [IAM full docs](https://cloud.google.com/iam/docs)
- [Understanding roles](https://cloud.google.com/iam/docs/understanding-roles)
- [Understanding custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles)
- [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access)
- [https://cloud.google.com/iam/docs/creating-custom-roles](https://cloud.google.com/iam/docs/creating-custom-roles)
- [Compute Engine IAM roles and permissions](https://cloud.google.com/compute/docs/access/iam)
- [Cloud Storage - Identity and Access Management](https://cloud.google.com/storage/docs/access-control/iam)
- [App Engine - Setting up access control](https://cloud.google.com/appengine/docs/standard/java/access-control)
