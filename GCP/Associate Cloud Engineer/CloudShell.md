
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

