# Best practices for enterprise organizations
[Reference](https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations)

## Organizational setup
### Define your resource hierachy
![](https://cloud.google.com/docs/images/best-practices-for-enterprise-organizations.png)

+ Why:
	+ Provide a hierarchy of ownership, which binds the lifecycle of a resource to its immediate parent in the hierarchy.
	+ Provide attach points and inheritance for access control and organization policies.
+ How:
	+ Thứ tự các cấp: Organization > Folders > Projects > Resources

Detail: [Resource Hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

### Create an Org node
Dùng [Cloud Identity](https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations#project-structure) để tạo Organization, vd: `sun.com`. Sau đó có thể migrate các existed project vào trong org.
### Specify your project structure
- *One project per application per environment*. VD: Có 2 app: `app1`, `app2`, mình nên tạo 4 projects: `app1-dev`, `app2-dev`, `app1-prd`, `app2-prd`. Tách biệt và sử dụng resources riêng sẽ tránh được việc ảnh hưởng lẫn nhau, áp dụng CI/CD cũng dễ hơn.

[Policy design for enterprise customer](https://cloud.google.com/solutions/policies/designing-gcp-policies-enterprise)

### Automate project creation
Sử dụng [Cloud Deployment Manager](https://cloud.google.com/deployment-manager), hoặc dùng Teraform, Ansible or Puppet.

## Identity and Access Management
### Manage Google identities
+ Google sử dụng Google account để authen + management.
	- Google account: gmail.com
	- Service account: gserviceaccount.com
	- Google group: googlegroups.com
	- G Suite - Cloud Identity domain: sun-asterisk.com
### Federate your identity provider with Google Cloud
Nếu công ty có hệ thống identity provider riêng, có thể sử dụng [đồng bộ lên Cloud Identity](https://cloud.google.com/solutions/authenticating-corporate-users-in-a-hybrid-environment) để access sử dụng credential của tổ chức.
### Control access to resources
Dùng IAM để control access vào các resource:

> Control *who* (identity) has *what access* (role) for *which* resource

Thay vì assign trực tiếp permission, chúng ta có thể assign role. Roles là tập hợp các permissions.

### Use groups and service accounts
Nên gom các users có same responsiblities vào 1 `groups` và assign IAM roles cho groups thay vì cho individual users.

[Service account](https://cloud.google.com/iam/docs/understanding-service-accounts) là 1 loại GG account. Có thể được assign IAM roles để access tới resources. Authenticate bằng key pair.
Nên dùng service account cho việc tương tác server-to-server

### Define an organization policy
Define an [organization policy service](https://cloud.google.com/resource-manager/docs/organization-policy/overview) để quản lý org resources.

## Networking and security

### Use VPC to define your network.
### Manage traffic with firewall rules.
### Limit external access.
### Centralize network control.
### Connect your enterprise network.
### Secure your apps and data.

## Logging, monitoring, and operations
### Centralize logging and monitoring.
### Set up an audit trail.
### Export your logs.
### Embrace DevOps and explore Site Reliability Engineering.

## Cloud architecture
### Plan your migration.
### Favor managed services.
### Design for high availability.
### Plan your disaster recovery strategy.

## Billing and management
### Know how resources are charged.
### Set up billing and permissions.
### Analyze and export your bill.
### Plan for your capacity requirements.
### Implement cost controls.
### Purchase a support package.
### Get help from the experts.
### Build centers of excellence.


## References
