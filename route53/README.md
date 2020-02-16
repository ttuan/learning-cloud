# AWS Route 53

## Introduction
Cần đáp ứng đủ 3 mục tiêu: availability, speed, và getting right content tới right users.

DNS: Making your resources available across a network using a human-readable name. Đảm bảo được các IP address ẩn đc phía sau những domain name dễ nhớ.

Route 53 được xây dựng như 1 manage domain services. -> đảm bảo tốc độ của resources.

CloudFront (CDN), đảm bảo tốc độ
## The Domain Name System
DNS có nhiệm vụ mapping domain name với IP address.
### Namespaces
Quản lý thông qua 1 `naming convention`. Vì nếu có nhiều trang web cùng dùng 1 domain, hoặc nhiều resource cùng có IP address giống nhau thì sẽ rất hỗn loạn.

Internet naming system được maintained với `domain name hierarchy` namespace, control cách dùng những tên human-readable. Những tên này được quản lý bởi ICANN.
### Name Servers
Nhiệm vụ của Name Server là là liên kết 1 domain name với 1 actual IP address. Trong mỗi máy tính sẽ có 1 name server database đơn giản. Nó sẽ map `hostname` với 1 IP address (sample có thể xem trong file /etc/hosts).

Từ máy local, request sẽ được đi qua local name server, xem trong file /etc/hosts này có đc thoả mãn không, nếu k request sẽ đc chuyển tới external DNS name servers. đc chỉ định trong network interface configuration (vd public DNS của Google 8.8.8.8) Từ đó nó sẽ trả về IP address match với domain name mình vừa nhập.
### Domains and Domain Names
Domain is one or more servers, data repositories, or other resources identified by a single domain name.

A domain name is a name that been regisstered for the domain that's used to direct network rquests to the domain's resource.
### Domain Registration
Các name servers cần đc đăng ký trước. Route 53 cũng là 1 domain registrar.
### Domain Layers
aws.amazon.com

+ `.com` is top-level domain (TLD)
+ `amazon` is second-level domain (SLD)
+ `aws.amazon.com` is subdomain.
### Fully Qualified Domain Names
Khi nhập 1 trang web nào đó, system default domain name sẽ tự động đc thêm vào. Ví dụ: workstation -> workstation.localhost. Để tránh, ta cần dùng fully qualified domain names.
### Zones and Zone Files
Zone (hosted zone) là 1 subset của DNS domain.

A zone file là 1 text file miêu tả cách resource với zone nên được map với DNS address của domain:
1 zone file records sẽ bao gồm: Name, TTL, Record Class, record type.
### Record Types
Ta nhập record type trong zone file ở mục trên. Nó sẽ chỉ ra cách mà record data được format và sẽ được sử dụng ntn.

Vd: A - Map hostname với 1 IPv4 address, CNAME - Cho phép bạn định nghĩa 1 hostname là alias của 1 thằng khác. MX: Mai exchange, map a domain với message transfer agents, ...
### Alias Records

## Amazon Route 53
Focus on: Domain registration, DNS management, availability monitoring (heal check), and routing policies (traffic management)
### Domain Registration
Ta đăng ký ở đâu cũng được. Tuy nhiên Route53 đơn giản hơn vì ta đang dùng AWS resource rồi.

Nếu ta đã đăng ký ở 1 chỗ khác, muốn chuyển sang Route53, ta cần: Unlocking the domain transfer setting trong registar's admin interface và request 1 authorization code. Sau đó supply code này vào Route 53.

Nếu ta muốn dùng Route53 để quản lý domain đã được hosted ở 1 external registar: Copy name server address included in your Route 53 record set and paste them as a new name server value in your registar's admin interface.
### DNS Management
Ta có thể config hosted zone qua console hoặc AWS CLI.
Sau khi tạo mới 1 hosted zone và nhập domain name, bạn cần nói Route 53 bạn muốn zone này đc public hay private hosted. Private thì chỉ hđ trong VPCs mà bạn chỉ định.

### Avalability Monitoring
Khi bạn tạo mới 1 record set, Ta sẽ đc chọn routing policy. 1 healcheck, đc tạo, config -> test resource, confirm là nó có healthy không. Nếu OK thì Route 53 sẽ routing traffic vào resource. còn nếu không, nó sẽ coi resource đang offline và chuyển traffic vào backup resource.
### Routing Policies
Default là simple policy. Nó sẽ chuyển mọi request tới IP address/domain name mà ta assign.

+ *Weighted Routing*: Phân bổ traffic về các resource dựa trên trọng số ta xet.
+ *Latency Routing*: Điều hướng tới region gần người dùng nhất để cho response nhanh nhất có thể. (Tập trung vào tốc độ phản hồi)
+ *Failover Routing*: Trỏ traffic vào primary resource (có check health check). Nếu primary go offline thì trỏ vào secondary resource.
+ *Geolocation Routing*: Dựa vào vị trí người gửi request để xác định sẽ gửi tới resource nào. (Tập trung vào nội dung hiển thị)
+ *multivalue Answer Routing*: Mỗi resource sẽ đc gắn 1 cái healcheck. Sau đó với traffic tới, Route 53 sẽ dùng healcheck để xem resources nào đang healthy, rồi random pass traffic về các resource healthy đó.
### Traffic Flow
1 graphic tool, cho phép ta xem được traffic sẽ ntn nếu dùng nhiều routing policies.

+ *Geoproximity Routing*: Gần giống với geolocation routing. Nó có thể chỉ ra geographic areas phù hợp với 1 địa điểm (lat, long)
## Amazon CloudFront
Giups chuyển content tới ng dùng 1 cách nhanh nhất có thể. Cached content at edge location to provide low-latency delivery.

Khi request, Route53 sẽ tự động điều hướng content request tới các CloudFront distribution xem cái nào hợp lý nhất dựa trên vị trí của người dùng.

Nếu đây là lần đầu tiên content này được requested qua endpoint, content sẽ được copy từ origin server. Những lần sau thì do content đã đc cache nên sẽ chuyển nhanh hơn nhiều.

Kind of CloudFront distribution phụ thuộc vào loại media.

+ Web page & graphic content: Web distribution
+ Video content in S3 bucket: RTMP.

We can add free SSL encryption certificate vào distribution.

Support: S3 bucket, AWS Mediapackage channel endpoint, AWS MediaStoreContainer endpoint.
## Summary
