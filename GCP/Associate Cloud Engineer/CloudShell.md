
# Gcloud shell

```sh

# ----------------------------
# Compute Engine
# ----------------------------


# VM Instances

# Check VM available
gcloud compute instances get-serial-port-output

# Create a VM instances
gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone $ZONE

# ----------------------------
gcloud config --help

gcloud config list
gcloud config list --all
gcloud components list

# Change to `gcloud interactive` mode to show completion
gcloud beta interactive

# SSH to your VM instance
gcloud compute ssh <instance-name> --zone $ZONE

# set your default compute zone
gcloud config set compute/zone us-central1-a

# ----------------------------
# Create a cluster
gcloud container clusters create [CLUSTER-NAME]

# authenticate the cluster,
gcloud container clusters get-credentials [CLUSTER-NAME]

# Create new deployment object
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
# create a Kubernetes Service
kubectl expose deployment hello-server --type=LoadBalancer --port 8080
# inspect service
kubectl get service
# Delete cluster
gcloud container clusters delete [CLUSTER-NAME]

# -----------------------
# Create instance-template
gcloud compute instance-templates create nginx-template \
         --metadata-from-file startup-script=startup.sh
# Create target pool
gcloud compute target-pools create nginx-pool
# Create managed instance group
gcloud compute instance-groups managed create nginx-group \
         --base-instance-name nginx \
         --size 2 \
         --template nginx-template \
         --target-pool nginx-pool

gcloud compute instances list

# Create firewall
gcloud compute firewall-rules create www-firewall --allow tcp:80


# ----------------------
# Create a network balancer
gcloud compute forwarding-rules create nginx-lb \
         --region us-central1 \
         --ports=80 \
         --target-pool nginx-pool

# List all Compute Engine forwarding rules in projects
gcloud compute forwarding-rules list

# ----------------------
# Create a HTTP(s) load balancer
# Create health-check
gcloud compute http-health-checks create http-basic-check
# Define an HTTP service, and map a port name to the relevant port for the instance group:
gcloud compute instance-groups managed \
      set-named-ports nginx-group \
      --named-ports http:80

# Create a backend service:
gcloud compute backend-services create nginx-backend \
      --protocol HTTP --http-health-checks http-basic-check --global

# Add the instance group to the backend service
gcloud compute backend-services add-backend nginx-backend \
   --instance-group nginx-group \
   --instance-group-zone us-east1-a \
   --global

# Create a default URL map that directs all incoming requests to all your instances:
gcloud compute url-maps create web-map \
   --default-service nginx-backend

# Create a target HTTP proxy to route requests to your URL map:
gcloud compute target-http-proxies create http-lb-proxy \
   --url-map web-map
# Create a global forwarding rule to handle and route incoming requests:
gcloud compute forwarding-rules create http-content-rule \
      --global \
      --target-http-proxy http-lb-proxy \
      --ports 80
# Run the following command to list your forwarding rules:
gcloud compute forwarding-rules list
```

HTTP(s) Load balancer rule is **global**
Network load balancer is regional, non-proxied load balancer.




## IAM

```sh
# IAM
# View the role metadata/ Describe a role
gcloud iam roles describe [ROLE_NAME]

# List all roles that can be applied to a given resource.
gcloud iam list-grantable-roles //cloudresourcemanager.googleapis.com/projects/$DEVSHELL_PROJECT_ID

# Create custom role from role definition.yaml file
gcloud iam roles create editor --project $DEVSHELL_PROJECT_ID --file role-definition.yaml

# Create using flags
gcloud iam roles create viewer --project $DEVSHELL_PROJECT_ID \
--title "Role Viewer" --description "Custom role description." \
--permissions compute.instances.get,compute.instances.list --stage ALPHA

# List custom roles
gcloud iam roles list --project $DEVSHELL_PROJECT_ID

# Update a role, remember create file file with etag value (which you get from describe command)
gcloud iam roles update [ROLE_ID] --project $DEVSHELL_PROJECT_ID --file new-role-definition.yaml

# Update by using flags
gcloud iam roles update viewer --project $DEVSHELL_PROJECT_ID --add-permissions storage.buckets.get,storage.buckets.list

# Change stage value to disable a custom role
gcloud iam roles update viewer --project $DEVSHELL_PROJECT_ID --stage DISABLED

# Delete a custom role
gcloud iam roles delete viewer --project $DEVSHELL_PROJECT_ID

# Undelete a role (< 7 day)
gcloud iam roles undelete viewer --project $DEVSHELL_PROJECT_ID

# =====================

# Create service account
gcloud iam service-accounts create my-sa-123 --display-name "my service account"

# Gain role for service account
gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
    --member serviceAccount:my-sa-123@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com --role roles/editor
```


## VPC Peering
```sh
# VPC Peering
# Create custom network
gcloud compute networks create network-a --subnet-mode custom

# Create a subnet within this VPC and specify a region and IP range
gcloud compute networks subnets create network-a-central --network network-a \
    --range 10.0.0.0/16 --region us-central1

# Create VM instances
gcloud compute instances create vm-a --zone us-central1-a --network network-a --subnet network-a-central

# enable SSH and icmp (Internet control message protocol
gcloud compute firewall-rules create network-a-fw --network network-a --allow tcp:22,icmp
```

Để peer được 2 thằng thì phải tạo được VPC network peering từ cả 2 project. 2 bên trỏ đến nhau =))

## App Engine

```sh
# App Engine

# Deploy with an app.yaml file
gcloud app deploy

# Browser app
gcloud app browse

# disable the Flex API
gcloud services disable appengineflex.googleapis.com
```

## Cloud Storage

```sh
# Cloud storage
gsutil mb gs://${BUCKET_NAME}

# Upload an object to bucket
gsutil cp OBJECT_NAME gs://YOUR-BUCKET-NAME

# Download an object from bucket
gsutil cp -r gs://YOUR-BUCKET-NAME/ada.jpg .

# Copy object to a folder
gsutil cp gs://BUCKET-NAME/ada.jpg gs://BUCKET-NAME/folder/

# List objects
gsutil ls gs://YOUR-BUCKET-NAME

# List detail
gsutil ls -l gs://YOUR-BUCKET-NAME/ada.jpg

# Update ACL for an object
gsutil acl ch -u AllUsers:R gs://YOUR-BUCKET-NAME/ada.jpg

# Remove ACL
gsutil acl ch -d AllUsers gs://YOUR-BUCKET-NAME/ada.jpg

# Remove object
gsutil rm gs://YOUR-BUCKET-NAME/ada.jpg

```

## KMS - Key Management Service

```sh
# Enable KMS
gcloud services enable cloudkms.googleapis.com

# Create KeyRing
gcloud kms keyrings create $KEYRING_NAME --location global

# Create CryptoKey from KeyRing
gcloud kms keys create $CRYPTOKEY_NAME --location global \
      --keyring $KEYRING_NAME \
      --purpose encryption

# Encrypt with KMS
curl -v "https://cloudkms.googleapis.com/v1/projects/$DEVSHELL_PROJECT_ID/locations/global/keyRings/$KEYRING_NAME/cryptoKeys/$CRYPTOKEY_NAME:encrypt" \
  -d "{\"plaintext\":\"$PLAINTEXT\"}" \
  -H "Authorization:Bearer $(gcloud auth application-default print-access-token)"\
  -H "Content-Type:application/json" \
| jq .ciphertext -r > 1.encrypted

curl -v "https://cloudkms.googleapis.com/v1/projects/$DEVSHELL_PROJECT_ID/locations/global/keyRings/$KEYRING_NAME/cryptoKeys/$CRYPTOKEY_NAME:decrypt" \
  -d "{\"ciphertext\":\"$(cat 1.encrypted)\"}" \
  -H "Authorization:Bearer $(gcloud auth application-default print-access-token)"\
  -H "Content-Type:application/json" \
| jq .plaintext -r | base64 -d

# Add role to manage KMS key
gcloud kms keyrings add-iam-policy-binding $KEYRING_NAME \
    --location global \
    --member user:$USER_EMAIL \
    --role roles/cloudkms.admin

# Add permission to encrypt/decrypt any CryptoKey which is created from your KeyRing
gcloud kms keyrings add-iam-policy-binding $KEYRING_NAME \
    --location global \
    --member user:$USER_EMAIL \
    --role roles/cloudkms.cryptoKeyEncrypterDecrypter

```
# Cloud Package Mirroring
```sh
# Create Virtual Private Network
gcloud compute networks create dm-stamford \
--subnet-mode=custom

# Add a subnet to the VPC for mirrored traffic in us-west4:
gcloud compute networks subnets create dm-stamford-uswest4 \
--range=172.21.0.0/24 \
--network=dm-stamford \
--region=us-west4

# Add a subnet to the VPC for the collector in us-west4:
gcloud compute networks subnets create dm-stamford-uswest4-ids \
--range=172.21.1.0/24 \
--network=dm-stamford \
--region=us-west4

------
# Create firewall rules
gcloud compute firewall-rules create fw-dm-stamford-allow-any-web \
--direction=INGRESS \
--priority=1000 \
--network=dm-stamford \
--action=ALLOW \
--rules=tcp:80,icmp \
--source-ranges=0.0.0.0/0

gcloud compute firewall-rules create fw-dm-stamford-ids-any-any \
--direction=INGRESS \
--priority=1000 \
--network=dm-stamford \
--action=ALLOW \
--rules=all \
--source-ranges=0.0.0.0/0 \
--target-tags=ids

gcloud compute firewall-rules create fw-dm-stamford-iapproxy \
--direction=INGRESS \
--priority=1000 \
--network=dm-stamford \
--action=ALLOW \
--rules=tcp:22,icmp \
--source-ranges=35.235.240.0/20

# Create Cloud NAT
## Create Cloud route
gcloud compute routers create router-stamford-nat-west4 \
--region=us-west4 \
--network=dm-stamford

## Config NAT
gcloud compute routers nats create nat-gw-dm-stamford-west4 \
--router=router-stamford-nat-west4 \
--router-region=us-west4 \
--auto-allocate-nat-external-ips \
--nat-all-subnet-ip-ranges

-----------
# Create VM
# Create instance-template
gcloud compute instance-templates create template-dm-stamford-web-us-west4 \
--region=us-west4 \
--network=dm-stamford \
--subnet=dm-stamford-uswest4 \
--machine-type=g1-small \
--image=ubuntu-1604-xenial-v20200807 \
--image-project=ubuntu-os-cloud \
--tags=webserver \
--metadata=startup-script='#! /bin/bash
  apt-get update
  apt-get install apache2 -y
  vm_hostname="$(curl -H "Metadata-Flavor:Google" \
  http://169.254.169.254/computeMetadata/v1/instance/name)"
  echo "Page served from: $vm_hostname" | \
  tee /var/www/html/index.html
  systemctl restart apache2'

# Create managed instance group for the WebServer
gcloud compute instance-groups managed create mig-dm-stamford-web-uswest4 \
    --template=template-dm-stamford-web-us-west4 \
    --size=2 \
    --zone=us-west4-a

# Create an Instance Template for the IDS VM
gcloud compute instance-templates create template-dm-stamford-ids-us-west4 \
--region=us-west4 \
--network=dm-stamford \
--no-address \
--subnet=dm-stamford-uswest4-ids \
--image=ubuntu-1604-xenial-v20200807 \
--image-project=ubuntu-os-cloud \
--tags=ids,webserver \
--metadata=startup-script='#! /bin/bash
  apt-get update
  apt-get install apache2 -y
  vm_hostname="$(curl -H "Metadata-Flavor:Google" \
  http://169.254.169.254/computeMetadata/v1/instance/name)"
  echo "Page served from: $vm_hostname" | \
  tee /var/www/html/index.html
  systemctl restart apache2'

# Create managed instance group for the IDS VM
gcloud compute instance-groups managed create mig-dm-stamford-ids-uswest4 \
    --template=template-dm-stamford-ids-us-west4 \
    --size=1 \
    --zone=us-west4-a


--------
# Create Internal LoadBalancer
# Create basic health check for the backend services
gcloud compute health-checks create tcp hc-tcp-80 --port 80

# Create a backend service group to be used for an ILB
gcloud compute backend-services create be-dm-stamford-suricata-us-west4 \
--load-balancing-scheme=INTERNAL \
--health-checks=hc-tcp-80 \
--network=dm-stamford \
--protocol=TCP \
--region=us-west4

# Add the created IDS managed instance group into the backend service group
gcloud compute backend-services add-backend be-dm-stamford-suricata-us-west4 \
--instance-group=mig-dm-stamford-ids-uswest4 \
--instance-group-zone=us-west4-a \
--region=us-west4

# Create a front end forwarding rule to act as the collection endpoint
 gcloud compute forwarding-rules create ilb-dm-stamford-suricata-ilb-us-west4 \
 --load-balancing-scheme=INTERNAL \
 --backend-service be-dm-stamford-suricata-us-west4 \
 --is-mirroring-collector \
 --network=dm-stamford \
 --region=us-west4 \
 --subnet=dm-stamford-uswest4-ids \
 --ip-protocol=TCP \
 --ports=all

----------
# Config Package Mirror Policy
gcloud compute packet-mirrorings create mirror-dm-stamford-web \
--collector-ilb=ilb-dm-stamford-suricata-ilb-us-west4 \
--network=dm-stamford \
--mirrored-subnets=dm-stamford-uswest4 \
--region=us-west4
```


## Kubernetes Cluster
```sh
# Create private cluster
gcloud beta container clusters create private-cluster \
    --enable-private-nodes \
    --master-ipv4-cidr 172.16.0.16/28 \
    --enable-ip-alias \
    --create-subnetwork ""

# List the subnet in default network
gcloud compute networks subnets list --network default

# Get information about the automatically created subnet
gcloud compute networks subnets describe [SUBNET_NAME] --region us-central1

# Create source instance which is used to check the connectivity to Kubernetes Network
gcloud compute instances create source-instance --zone us-central1-a --scopes 'https://www.googleapis.com/auth/cloud-platform'

# Get External IP
gcloud compute instances describe source-instance --zone us-central1-a | grep natIP

# Authorize your external address range with the CIDR range of the external addresses
gcloud container clusters update private-cluster \
    --enable-master-authorized-networks \
    --master-authorized-networks [MY_EXTERNAL_RANGE](ip/32)

# SSH to source instance
gcloud compute ssh source-instance --zone us-central1-a

# Configure access to the Kubernetes cluster from SSH shell
gcloud container clusters get-credentials private-cluster2 --zone us-central1-a

# Verify that your cluster nodes do not have external IP addresses
kubectl get nodes --output yaml | grep -A4 addresses

# Delete cluster
gcloud container clusters delete private-cluster --zone us-central1-a

-------
# Create a subnetwork and secondary range
gcloud compute networks subnets create my-subnet \
    --network default \
    --range 10.0.4.0/22 \
    --enable-private-ip-google-access \
    --region us-central1 \
    --secondary-range my-svc-range=10.0.32.0/20,my-pod-range=10.4.0.0/14

# Create private cluster use above subnetwork
gcloud beta container clusters create private-cluster2 \
    --enable-private-nodes \
    --enable-ip-alias \
    --master-ipv4-cidr 172.16.0.32/28 \
    --subnetwork my-subnet \
    --services-secondary-range-name my-svc-range \
    --cluster-secondary-range-name my-pod-range
```
