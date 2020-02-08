# VPC - Virtual Private Cloud

Amazon VPC lets you provision a logically isolated section of AWS cloud where
you can launch AWS resources in a virtual network. (Networking, IP address
range, subnets, route tables, network gateways, security settings, ...)


Subnet:
- A subnet is a range of IP address in your VPC. A public subnet must be
    connected to the Internet. A private subnet for resources that won't be
    connected to the Internet.

- A public subnet must have an Internet Gateway, so that traffic can access your
    web server.


Internet Gateway
- Allow communication between instances in VPC with and Intenet. It therefore
    imposes no availability risks or bandwidth constraints on your network
    traffic.

purposes:
+ Provide a target in VPC route tables for Internet routable traffic.
+ Perform network address translation (NAT) for instances which have been
    assigned public IPv4 address.


A VPC Gateway Attachment
- Creates a relationship between a VPC and a gateway, such as this Internet Gateway.


Route Table
- Contain a set of rules - called routes. Used to determine where network
    traffic is directed. Each subnet in VPC must be associated with a route
    table.

If a subnet is associated with a route table, that has a route to the Internet
Gateway, it's known a public subnet.

Availability Zones
- Additional public and private subnets have been added in another Availability Zone. This is best practice to ensure that your resources can run in multiple data centers (Availability Zones) to ensure High Availability in case of system failures.


Create VPC, Subnet, Internet Gateway.
Create route table. Add route 0.0.0.0/0 to connect Internet Gateway. Add subnet
to this route table.
=> Now your subnet is public subnet.


EndPoint vs EndPointService???

You can’t change the primary CIDR for a VPC, so you must create a new one to connect it to your internal network.
The definition of a public subnet is a subnet that has a default route pointing to an Internet gateway as a target. Otherwise, it’s a private subnet.


VPC is at network layer, in EC2 is instance level.
VPC exist only with an region. VPC support is not support for some regions.

## VPC CIRD
Mỗi VPC phải có ít nhất 1 dải IP, gọi là CIDR block
prefix length càng nhỏ thì dải IP đó càng có nhiều IP aAddress
Valid IPV4 là từ /0 -> /32
Theo RFC1918, nên dùng 3 dải IP sau để tránh conflict với public IP Address:
192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12
Nếu muốn connect 2 VPC với nhau, cần chắc chắn là dải IP của 2 thằng k bị
overlap.
Sau khi tạo VPC, không thay đổi được primary CIDR block.

#### Secondary CIDR Block
Mỗi VPC có 1 primary CIDR, nhưng có thể có nhiều secondary CIDR blocks. Yêu cầu
là nó phải có cùng address range với primary CIDR và không overlap với primary
CIDR hoặc các secondary CIDR khác.
VD: Nếu bạn set primary CIDR là: 192.168.0.0/16, bạn sẽ không thể tạo secondary
CIDR trong tương lai.

#### IPV6 CIDR Block
- KHông được tự chọn IP prefix, nó sẽ đc AWS cấp phát.
- Prefix length luôn là /56


## Subnet
- Là 1 logical container giữ EC2
- Cô lập instance này với thằng khác, control traffic bằng functions
- Mọi instance phải thuộc 1 subnet. Không move nó qua subnet/VPC khác, trừ khi
    xoá đi tạo lại.

#### Subnet CIDR blocks
- Là subset của VPC CIDR
- KHông assign được 4 address đầu và 1 address cuối cho instance.
- 1 khi đã tạo subnet thì khôgn thay đổi được CIDR.
- Vì 1 VPC có thể cso nhiều subnet, nên prefix length của subnet CIDR nên lớn
    hơn của VPC, để sau này còn có thể tạo thêm subnet.
- Subnet không có nhiều CIDR, nhưng nó có thể ăn ké secondary CIDR của VPC.

#### Availability Zones
- Mỗi subnet chỉ nằm trên 1 AZ. Để tăng tính resilient, nên tạo mỗi subnet trên
    1 AZ, để nếu 1 AZ toang thì những subnet còn lại vẫn hoạt động được.
- Subnet phải nằm trên AZ thuộc VPC region.


#### IPV6 CIDR Blocks
- Prefix length của VPC là /56, còn của Subnet là /64
- Luôn phải asign IPv4 CIDR cho subnet, ngay cả khi không dùng.


## Elastic Network Interfaces
- Mỗi instance đều có 1 ENI để kết nối với resource khác. Nhờ nó mà chúng ta có
    thể SSH vào trong instance được.
- Mỗi primary ENI này được connect tới chỉ 1 subnet. Đó là lý do tại sao khi tạo
    instance, chúng ta phải chọn subnet.

#### Primary & Secondary Private IP Address
- Private IP phụ thuộc vào subnet CIDR
- Có thể attach thêm ENI vào bên trong instance, tuy nhiên subnet đó phải thuộc
    cùng AZ với instance.

#### Attaching ENI
- ENI tách biệt với instance, nên xoá instance cũng k xoá ENI
- Nếu 1 instance bị fail, tháo ENI ra, lắp vào instance hoạt động để điều hướng
    traffic tới instance mới.

## Internet Gateway
- Cho phép instance có public IP để vào Internet.
- Mỗi 1 VPC chỉ có 1 IG
- Để dùng được, cần có default route và route table. Packet từ Internet trả về
    sẽ qua IG, sau đó nó soi xem route table để biết request sẽ về instnace
    private nào.

## Route table.
- Mỗi subnet phải có 1 route table, nhưng 1 routable có thể có nhiều subnet.
- Khi tạo VPC, aws tạo sẵn 1 "main-route-table", và liên kết nó vs mọi subnet
    trong VPC.

#### Routes
- Route này như là 1 rule, rule này sẽ điều hướng xem network sẽ đi đâu về đâu.
- Gồm 2 phần là Destination (IP prefix hoặc CIDR notation), và Target (IG hoặc
    ENI)

#### The Default Route
- Để instance có thể truy cập vào internet, ta cần tạo default route trỏ tới
    Internet Gateway.
- Route chọn thằng map gần nhất để điều hướng. Ví dụ route đi ra ngoài internet
    có destination là 0.0.0.0, còn route local là 172.31.0.0/16, 2 cái này
    overlap với nhau, nhưng route sẽ chọn thằng gần nhất với địa chỉ IP mà
    packet cần đến để gửi.
- Public subnet có default route còn private subnet thì không.

## Security Group
- Mọi ENI cần phải liên kết với ít nhất 1 SG.
- Inbound Rule gồm source, protocol, port range. SG default deny tất cả các
    request.
- Outbound thường sẽ là đi ra ngoài internet, không cấm gì cả.

#### Source and Destinations
- Nên assign same SG để instance giao tiếp với nhau dễ hơn

#### Statefull Firewall
- SG là statefull. Tức là khi SG cho phép traffic vào, thì nó cũng cho phép
    reply traffic theo chiều ngược lại.

#### The default SG
- Mỗi VPC đều có 1 default SG. Nó tạo ra để nếu mình có launch instance thì còn
    cso SG mà attach vào :v

## Network Access Control Lists
- VPC có 1 default NACL
- NACL đươc attahc vào subnet, SG được attach vào ENI
- NACL can't control traffic between instance in same subnet.
- 1 NACL có thể được dùng cho nhiều subnet.
- NACL is stateless, SG is statefull.


#### Inbound Rules
- Rule được sắp xếp theo thứ tự tăng dần của Rule Number. lọc dần các request từ
    trên xuống. Rule cuối thường sẽ deny tất cả những request không match với
    những rule bên trên.
- rules bao gồm: Rule number, Protocol, Port range, source, action.


#### Outbound Rules
- Rule giống với Inbound rule, khác mỗi thay source thành destination.
- Vì NACL là stateless nên nếu inbound mà cho phép HTTPS thì outbound cũng cần
    có rule cho phép HTTPS đi ra. Tuy nhiên, nếu client send request HTTPS tới
    instance của ta qua port 80, cient nó sẽ nghe ở port 36034. Chúng ta không
    chắc nó sẽ nghe response trên cổng nào để mà mở outbound port được => Không
    nên restrict outbound traffic bằng NACL.

#### Using NACL vs SG
- Khi người dùng chạy instance thì nó chọn SG. Nếu ta k muốn bị phụ thuộc vào
    user thì nên sử dụng NACL vì nó đc apply vào trong subnet.
- Không nên thay đổi NACL vs SG song song, vì khó debug.
- Source/Destination trong NACL chọn CIDR còn SG có thể chọn SG khác.

## Public IP Address
- Khi bạn chạy 1 instance vtrong 1 subnet, sẽ có option để sinh public IP cho
    instance đó. Nếu instance không cần đi ra ngoài internet thì k cần chọn
    option này.
- Khi instance stop & start, public IP sẽ bị thay đổi.


## Elastic IP
- EIP là rời rạc, có thể gắn vào ENI này hoặc ENI khác.
- Nếu EIP mà đc assign vào 1 ENI đã có public IP thì AWS sẽ replace public IP đó
    bằng EIP

## Network Address Translation
- NAT là quá trình Internet Gateway map public IP address với ENI's private IP.
- NAT chỉ có 2 thằng là Source và Destination IP Address. Route table thì cần
    nhiều hơn, nó cho phép config 1 dải IP.

## NAT Devicé
- Bao gồm NAT gateway và NAT instance
- Instance không có public IP (nên k giao tiếp đc với Internet), nếu muốn fetch
    update thì sẽ cần có NAT device.
- NAT device được config public IP, giúp nó có thể truy cập internet.


#### Configure Route Tables to Use NAT Devices
- Instance phải sử dụng default route khác nhau. Vì target instance gửi tới NAT còn NAT
    gửi tới Internet.

#### NAT Gateway
- NAT Gateway chỉ nằm bên trong 1 subnet.
- Không có nhiều thứ để quản lý (giống Internet Gateway) => Just set and forget.
- Assign EIP cho nó. Muốn cho AZ khác cần tạo 1 NAT gateway khác, do NAT Gateway
    chỉ nằm bên trong 1 subnet.
- Tạo Gateway, sau đó tạo route default.
- NAT Gateway không có ENI -> không dùng được SG, chỉ dùng được NACL.
- NAT Gateway tự động scale để đáp ứng được với bandwidth requirements.


#### NAT Instance
- Là instance thường nên không tự động scacle để đáp ứng bandwidth requirement
- Có ENI -> Add được SG
- Phải disable Source/Destination check trong ENI để nó có thể gửi traffic của 1
    source IP khác. (IP của instance trong private subnet)
- Có thể dùng NAT instance như 1 bastion host. (jump server)
- Mình không thể tạo nhiều default route pointing to different NAT instances =>
    Thông thường, ng ta thích dùng NAT Gateway hơn NAT Instance.

## VPC Peering
- Dùng khi mình muốn comunication giữa các VPC qua private AWS network. các
    instance nằm ở different regions.
- point-to-point connection, nên chỉ connect được 2 VPC. Và CIDR của 2 VPC này k
    đc overlap.
- VPC peering allow only instance-to-instance connection.
- 2 instance connect với nhau không thể share được INternet Gateway hay NAT
    devices, nhưng có thể share Network Load Balancer.
- Nếu muốn transitive routing (tạo ra 1 chuỗi các VPC connect với nhau), bạn k
    thể dùng VPC peering, nhưng có thể tạo nhiều cặp VPC peering.
- Sử dụng AWS internal network, không phải qua Internet nên k cần public IP.
- Cần config SG chuẩn, cho phép Bi-direction comunication giữa 2 instance đó.
