# Platform Overview

[Google Cloud - Cloud Basic](https://cloud.google.com/docs/overview)

## Concepts
- Google Cloud resources: Giống như bên AWS, chia thành các `region` và `zone`
- [Google Cloud Products](https://cloud.google.com/products)
- Global Resources: Disk images, disk snapshots, network. Regional Resources: Static external IP. Zonal Resources: VM instances, their types, and disks.

- Project:
	+ Project Name: Tuỳ ý
	+ Project ID: Global uniq, mình đưa ra / GG tự sinh, sẽ được dùng trong SDK. Project có thể bị xoá nhưng prj id không bao giờ có thể sử dụng lại.
	+ Project Number: GG sinh ngẫu nhiên

- Có 3 cách để tương tác với GG Cloud: Qua web console, qua command-line interface ([Cloud SDK](https://cloud.google.com/sdk/docs) or [Cloud Shell](https://cloud.google.com/shell/docs/features)) and [client libraries](https://cloud.google.com/sdk/cloud-client-libraries)

## Services
### 1. Computing and hosting
+ Serverless computing:
	- Sử dụng [Cloud Functions](https://cloud.google.com/functions/docs/concepts/overview) - Function as a services (FaaS), chỉ support Python 3, Javascript, Go, Java.
	- Sử dụng tốt khi cần xử lý data, ELT operations (video transcoding/ IoT streaming data). Hoặc làm webhooks cho HTTP triggers, mobile backend functions, ...
+ Application platform:
	- [App Engine](https://cloud.google.com/appengine/docs) (PaaS), không phải suy nghĩ nhiều =))
	- Build app bằng Go, Java, .NET, Node.js, PHP, Python, Ruby
	- Google manage hosting, scaling, monitoring, infrastructure.
	- Tận dụng Redis, Cloud SQL, Cloud Storage, Web Security Scanner
+ Containers
	- Focus vào code, không cần lo deployments & integration, Sử dụng [Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) - Google Cloud's containers as a services (CaaS)
+ Vitual machines
	- Sử dụng Compute Engine - IaaS.

Có thể kết hợp nhiều loại lại với nhau để tận dụng được thế mạnh của từng loại.
### 2. Storage
- [Cloud Storage](https://cloud.google.com/storage) có vài loại, giảm dần theo giá và mức độ availability: Normal, Nearline (< 1 months), Coldline (< 1 quý), Archive (< 1 năm).
- Có thể lưu luôn trên đĩa của Compute Engine
- Có thể quản lý file thông qua [Filestore](https://cloud.google.com/filestore/docs).

### 3. Databases
[Cloud SQL](https://cloud.google.com/sql/docs) (MySQL and PostgreSQL). [Cloud Spanner](https://cloud.google.com/spanner/docs). NoSQL: [Firestore](https://cloud.google.com/firestore/docs/overview) and [Cloud Bigtable](https://cloud.google.com/bigtable/docs/overview)
### 4. Networking
+ Networks, firewalls and routes: [VPC](https://cloud.google.com/vpc/docs), [Firewall rules](https://cloud.google.com/vpc/docs/firewalls) and [route](https://cloud.google.com/vpc/docs/routes)
+ [Load balancing](https://cloud.google.com/load-balancing/docs):
	+ [Network load balancing](https://cloud.google.com/load-balancing/docs/network): Phân bổ trafic giữa các instances trong cùng 1 region dựa trên IP protocol data.
	+ [HTTP(S) load balancing](https://cloud.google.com/load-balancing/docs/https): Phân bổ traffic giữa các regions, đảm bảo request tới regions gần nó nhất, hoặc tới healthy instance ở region gần nhất. Có thể [phân bổ traffic dựa trên content type](https://cloud.google.com/load-balancing/docs/https/content-based-example), vd chuyển static content, image, css tới 1 server asset.
+ [Cloud DNS](https://cloud.google.com/dns/docs)

Ngoài ra còn có nhiều các connect khác: [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect), [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn), [Direct peering](https://cloud.google.com/network-connectivity/docs/direct-peering), [Carrier Peering](https://cloud.google.com/network-connectivity/docs/interconnect/carrier-peering/carrier-peering)

### 5. Big data
+ Data analysis: [BigQuery](https://cloud.google.com/bigquery/what-is-bigquery) - Tự tạo bảng từ nhiều service khác nhau, sau đó query dạng SQL-like
+ Batch and streaming data processing: [](https://cloud.google.com/dataflow/what-is-google-cloud-dataflow)
+ Asynchronous messaging: [Pub/Sub](https://cloud.google.com/pubsub/docs) - Gần giống thằng SNS bên aws, gửi JSON data.

### 6. Machine Learning
+ Machine learning APIs: [Video Intelligence API](https://cloud.google.com/video-intelligence/docs), [Speech to Text](https://cloud.google.com/speech/docs), [Cloud Vision](https://cloud.google.com/vision/docs), [Cloud Natural Language API](https://cloud.google.com/natural-language/docs), [Cloud Translation](https://cloud.google.com/translate/docs), [Dialogflow](https://cloud.google.com/dialogflow/docs)
+ [API Platform](https://cloud.google.com/ml-engine/docs/technical-overview)

## Tools
[Tools](https://cloud.google.com/products/tools)

## Others
* [Google Cloud for AWS Professionals](https://cloud.google.com/docs/compare/aws)
* [Search all docs tutorials](https://cloud.google.com/docs/tutorials)
* [Getting started with Ruby](https://cloud.google.com/ruby/getting-started)
