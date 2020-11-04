# Best practices for enterprise organizations
[Reference](https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations)

## Organizational setup
### Define your resource hierachy
![](https://cloud.google.com/resource-manager/img/cloud-folders-hierarchy.png)

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
- Dùng VPC để group các related resources
- VPC network là global resources, có thể span nhiều regions mà k cần communicateing over public internet.
- VPC chưa nhiều subnetworks. Mỗi subnetwork này cần phải define IP address range. Subnet là regional resources, và chỉ nằm trên 1 region.

### Manage traffic with firewall rules.
- Mỗi VPC network đc cài 1 virtual firewall, bảo vệ ở virtual networking level, là stateful

### Limit external access.
- Resources nằm trong subnet, sẽ được cấp internal IP từ dải IP của subnet, từ đó có thể giao tiếp với nhau (based on firewall rules)
- Để connect ra ngoài, resources cần public, external IP hoặc dùng [Cloud NAT](https://cloud.google.com/nat/docs/overview).

### Centralize network control.
- Dùng [Shared VPC](https://cloud.google.com/vpc/docs/shared-vpc) để connect các VPC network. Chú ý subnets, routes, firewalls

### Connect your enterprise network.
Nếu công ty có hệ thống on-premises.

+ Nếu cần low-latency, HA, ... thì dùng [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect) - đường truyền riêng, nối từ on-premise với cloud ??
+ Không quan trọng lắm với low-latency thì dùng [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn), setup encrypted IPsec VPN.

### Secure your apps and data.
- Dùng mấy hê thống check sec của GG :v

## Logging, monitoring, and operations
### Centralize logging and monitoring.
- Nên dùng [Cloud Logging](https://cloud.google.com/logging/docs) và [Cloud Monitoring](https://cloud.google.com/monitoring/docs) để theo dõi, phân tích log, view, search, ânlyze, alert. Có thể cài [agent](https://cloud.google.com/logging/docs/agent) vào các instance bên aws/on-premise để theo dõi.

### Set up an audit trail.
- Cài [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit) để biết được: Ai đã làm gì, ở đâu và khi nào =)) Nhớ cài IAM để control ai được xem audit logs.

### Export your logs.
- Log có thể bị xoá sau xx ngày, nên tốt nhất là export ra cloud storage, bigquery, pub/sub, ..

### Embrace DevOps and explore Site Reliability Engineering.
- Google support nhiều tool để giúp cho việc devops, vd: [source repositories](https://cloud.google.com/source-repositories), [CD tooling](https://cloud.google.com/solutions/continuous-delivery)

## Cloud architecture
### Plan your migration.
- Cần cân nhắc giữa: `lift-and-shift`, `transform-and-move`, `per-app basis`. [Migration center](https://cloud.google.com/solutions/migration-center)
- Có thể để 1 nửa trên GG cloud, 1 nửa ở on-premise. -> [hybrid cloud](https://cloud.google.com/solutions/manage-hybrid-cloud). Checkout: [patterns and best practices](https://cloud.google.com/solutions/hybrid-and-multi-cloud-patterns-and-practices)

### Favor managed services.
- Nên dùng các service có sẵn của GCP để dễ quản lý, quan sát :v

### Design for high availability.
- Distribution of compute resources, load-balancing and replication of data. Vd đặt Compute Engine ở nhiều region khác nhau =)) ([Reference](https://cloud.google.com/solutions/best-practices-compute-engine-region-selection))

### Plan your disaster recovery strategy.
- [Disaster recovery planning guide](https://cloud.google.com/solutions/dr-scenarios-planning-guide) - Chuẩn bị sẵn sàng khi gặp thảm hoạ.

## Billing and management
### Know how resources are charged.
- Dùng bao nhiêu giây, lưu trữ bao nhiêu, số lượng operations thực hiện, ...

### Set up billing and permissions.
1 billing account có thể được connect với nhiều projects, nhưng 1 project chỉ có 1 billing account.

## References
- [Resource Hierachy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)
- [Design GCP policies enterprise](https://cloud.google.com/solutions/policies/designing-gcp-policies-enterprise)
