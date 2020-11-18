# Container Optimized OS

Container-Optimized OS is an operating system image for your Compute Engine VMs that is optimized for running Docker containers, and is Google's recommended OS for running containers on Google Cloud.

## Container-Optimized OS benefits
* Run Containers Out of the Box: Container-Optimized OS instances come pre-installed with the Docker runtime and cloud-init. With a Container-Optimized OS instance, you can bring up your Docker container at the same time you create your VM, with no on-host setup required.

* Smaller attack surface: Container-Optimized OS has a smaller footprint, reducing your instance's potential attack surface.

* Locked-down by default: Container-Optimized OS instances include a locked-down firewall and other security settings by default.

* Automatic Updates: Container-Optimized OS instances are configured to automatically download weekly updates in the background; only a reboot is necessary to use the latest updates.


## Use Cases
* Container-Optimized OS can be used to run most Docker containers. You should consider using Container-Optimized OS as the operating system for your Compute Engine instance if you have the following needs:

* You need support for Docker containers or Kubernetes with minimal setup.

* You need an operating system that has a small footprint and is security hardened for containers.

* You need an operating system that is tested and verified for running Kubernetes on your Compute Engine instances.


```sh
# List all available images
gcloud compute images list \
    --project cos-cloud \
    --no-standard-images
# Use the gcloud compute instances create command with --image and --image-project flags to create a cos node image instance
gcloud beta compute instances create-with-container containerized-vm2 \
     --image cos-stable-72-11316-136-0 \
     --image-project cos-cloud \
     --container-image nginx \
     --container-restart-policy always \
     --zone us-central1-a \
     --machine-type n1-standard-1

# Create firewall rules
gcloud compute firewall-rules create allow-containerized-internal\
  --allow tcp:80 \
  --source-ranges 0.0.0.0/0 \
  --network default
```

# Google Cloud Video Intelligence
Google Cloud Video Intelligence makes videos searchable and discoverable by extracting metadata with an easy to use REST API. You can now search every moment of every video file in your catalog. It quickly annotates videos stored in Cloud Storage, and helps you identify key entities (nouns) within your video; and when they occur within the video. Separate signal from noise by retrieving relevant information within the entire video, shot-by-shot, -or per frame.


# Cloud Security Scanner
The Cloud Security Scanner identifies security vulnerabilities in your Google App Engine web applications. It crawls your application, following all links within the scope of your starting URLs, and attempts to exercise as many user inputs and event handlers as possible.

The scanner is designed to complement your existing secure design and development processes. To avoid distracting developers with false positives, the scanner errs on the side of under reporting and will not display low confidence alerts. It does not replace a manual security review, and it does not guarantee that your application is free from security flaws.

# Data lost Prevention
The Data Loss Prevention API provides programmatic access to a powerful detection engine for personally identifiable information (PII) and other privacy-sensitive data in unstructured data streams.

The DLP API provides fast, scalable classification and optional redaction for sensitive data elements like credit card numbers, names, social security numbers, passport numbers, and phone numbers. The API supports text and images – just send data to the API or specify data stored on your Cloud Storage, BigQuery, and Cloud Datastore instances.

In this lab you will set up the Data Loss Prevention API and and use the API to inspect a string of data for sensitive information.

# Kubernetes

Deployments - a replicated, stateless application on your cluster

Pods - the smallest deployable unit in Kubernetes

Services - allow your application to receive traffic

Autoscaling pods - scale the application based on load or custom metrics
