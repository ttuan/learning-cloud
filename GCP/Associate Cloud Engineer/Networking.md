# Networking

[Identity-Aware Proxy](https://cloud.google.com/iap/) to restrict access to selected users there are no changes necessary to the application

App Engine has its standard and flexible environments which are optimized for different application architectures. Currently, when enabling IAP for App Engine, if the Flex API is enabled, GCP will look for a Flex Service Account. Your Qwiklabs project comes with a multitude of APIs already enabled for the purpose of convenience. However, this creates a unique situation where the Flex API is enabled without a Service Account created.

```sh
gcloud services disable appengineflex.googleapis.com
```

IAP sẽ add 1 header vào trong request: `X-Goog-Authenticated-User-Email` => Cái này dễ bị fake

=> If there is a risk of IAP being turned off or bypassed, your app can check to make sure the identity information it receives is valid. This uses a third web request header added by IAP, called X-Goog-IAP-JWT-Assertion. The value of the header is a cryptographically signed object that also contains the user identity data. Your application can verify the digital signature and use the data provided in this object to be certain that it was provided by IAP without alteration.

Digital signature verification requires several extra steps, such as retrieving the latest set of Google public keys. You can decide whether your application needs these extra steps based on the risk that someone might be able to turn off or bypass IAP, and the sensitivity of the application.


## VPC

```
gcloud compute networks create managementnet --project=qwiklabs-gcp-01-d3560e7350f8 --subnet-mode=custom --mtu=1460 --bgp-routing-mode=regional

gcloud compute networks subnets create managementsubnet-us --project=qwiklabs-gcp-01-d3560e7350f8 --range=10.130.0.0/20 --network=managementnet --region=us-central1


gcloud compute networks create privatenet --subnet-mode=custom
gcloud compute networks subnets create privatesubnet-us --network=privatenet --region=us-central1 --range=172.16.0.0/24

gcloud compute networks subnets create privatesubnet-eu --network=privatenet --region=europe-west1 --range=172.20.0.0/20

gcloud compute networks list

gcloud compute networks subnets list --sort-by=NETWORK

gcloud compute --project=qwiklabs-gcp-01-d3560e7350f8 firewall-rules create managementnet-allow-icmp-ssh-rdp --direction=INGRESS --priority=1000 --network=managementnet --action=ALLOW --rules=tcp:22,tcp:3389,icmp --source-ranges=0.0.0.0/0

gcloud compute firewall-rules list --sort-by=NETWORK


gcloud beta compute --project=qwiklabs-gcp-01-d3560e7350f8 instances create managementnet-us-vm --zone=us-central1-c --machine-type=f1-micro --subnet=managementsubnet-us --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=1035118716137-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --image=debian-10-buster-v20201112 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=managementnet-us-vm --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any

gcloud compute instances create privatenet-us-vm --zone=us-central1-c --machine-type=n1-standard-1 --subnet=privatesubnet-us

gcloud compute instances list --sort-by=ZONE
```

Auto mode networks create subnets in each region automatically, while custom mode networks start with no subnets, giving you full control over subnet creation

The number of interfaces allowed in an instance is dependent on the instance's machine type and the number of vCPUs. The n1-standard-4 allows up to 4 network interfaces.

-------------
Authenticate service account with json key
gcloud auth activate-service-account --key-file credentials.json

Network Admin role - List firewall rules
Secure Admin role - List/Create/Delete/Modify firewall rules

## HTTP Load Balancer

Google Cloud HTTP(S) load balancing is implemented at the edge of Google's network in Google's points of presence (POP) around the world. User traffic directed to an HTTP(S) load balancer enters the POP closest to the user and is then load balanced over Google's global network to the closest backend that has sufficient capacity available.

Cloud Armor IP allowlist/denylist enable you to restrict or allow access to your HTTP(S) load balancer at the edge of the Google Cloud, as close as possible to the user and to malicious traffic. This prevents malicious users or traffic from consuming resources or entering your virtual private cloud (VPC) networks.

![](https://cdn.qwiklabs.com/7wJtCqbfTFLwKCpOMzUSyPjVKBjUouWHbduOqMpfRiM%3D)

Use `sudo apt-get -y install siege` to install siege for stress test.


## Internal Load Balancer

Google Cloud offers Internal Load Balancing for your TCP/UDP-based traffic. Internal Load Balancing enables you to run and scale your services behind a private load balancing IP address that is accessible only to your internal virtual machine instances.

In this lab, you create two managed instance groups in the same region. Then, you configure and test an Internal Load Balancer with the instances groups as the backends, as shown in this network diagram:

![](https://cdn.qwiklabs.com/k3u04mphJhk%2F2yM84NjgPiZHrbCuzbdwAQ98vnaoHQo%3D)

Health checks determine which instances of a Load Balancer can receive new connections. For Internal load balancing, the health check probes to your load balanced instances come from addresses in the ranges 130.211.0.0/22 and 35.191.0.0/16. Your firewall rules must allow these connections.

An instance template is an API resource that you can use to create VM instances and managed instance groups. Instance templates define the machine type, boot disk image, subnet, labels, and other instance properties.

Config IP để trỏ vào (Có thể là internet gateway). => 2 instances group (tạo từ instance template). 2 instance group này nằm ở 2 subnet khác nhau. => Config ILB rules
