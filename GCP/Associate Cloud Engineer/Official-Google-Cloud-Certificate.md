# Official Google Cloud Certificate Book

## Chapter 1. Overview of GCP
### Types of Cloud Services
#### 1. Compute Resources
1. Virtual Machines

	Google Cloud Platform offers a variety of preconfigured VMs with varying numbers of vCPUs and amounts of memory. You can also create a custom configuration if the preconfigured offerings do not meet your needs. A VM that you manage is like having a server in your office that you have full administrator rights to.

2. Managed Kubernetes Clusters

	Tools you need to create and manage clusters of servers. Allow users focus on their applications and not the tasks needed to keep a cluster of servers up and running.
Managed clusters make use of containers. The services are deployed through containers, and the cluster management service takes care of monitoring, networking, and some security management tasks.

3. Serverless Computing

	An approach that allows developers and application administrators to run their code in a computing environment that does not require setting up VMs or kubernetes clusters: **App Engine** (extended periods of time - website backend, point of sale system, custom business app) and **Cloud Functions** (code response to an event - upload a file, add a message to queue, ..)


#### 2. Storage
1. Object storage
	- A system that manages the use of storage in terms of objects or blobs. **Usually these objects are files, but it is important to note that the files are not stored in a conventional file system**. Objects are grouped into buckets. Each object is individually addressable, usually by a URL.
   - Serverless. There is no need to create VMs and attach storage to them.
   - Access controls can be applied at the object level.

2. File storage
	- A hierarchical storage system for files. Provides network shared file systems. **Cloud Firestore**: based on Network File System.
	- Suitable for application that require operating system-like file access to files.

3. Block storage
	- Uses a fixed-size data structure called a block to organize data. Block storage is commonly used in **ephemeral and persistent disks attached to VMs**.
	- A persistent disk: Store data even it detached form VM. Ephemeral disks exist and store data only as long as a VM is running.

4. Caches
	- In-memory data stores that maintain fast access to data.
	- Expensive, can lose data when power is lost, OS rebooted; can get out of sync with the system data.


#### 3. Networking
Need to control IP addresses, internal & external IP, firewall rules, peering VPC

#### 4.  Specialized Services
+ Serverless; you do not need to configure servers or clusters.
+ Provide a specific function, such as translating text or analyzing images.
+ AutoML, Cloud Natural Language, Cloud Vision, Cloud Inference API

### Cloud Computing vs Data Center Computing
#### 1. Rent Instead of Own Resources
- Spend a significant amount of money up front to purchase equipment or commit to a long-term lease for the equipment
- Hard to autoscale

#### 2. Pay-as-You-Go-for-What-You-Use Model
#### 3. Elastic Resource Allocation

## Chapter 2. Google Cloud Computing Services
### Computing Components of Google Cloud Platform
+ Computing resources
+ Storage resources
+ Databases
+ Networking services
+ Identity management and security Development tools
+ Management tools Specialized services

#### 1. Computing Resources
- IaaS: Compute Engine
- Paas: App Engine and Cloud Function
- Cluster: Kubernetes -> Managing containers

	a. Compute Engine: VMs are abstractions of physical servers. Ms run within a low-level service called a hypervisor. Hypervisors can run multiple operating systems, referred to as guest operating systems. Making a VM preemptible, charge less for the VM than normal (around 80%), but your VM could be shut down at any time by Google. (preemptible VM has run for at least 24 hours)

	b. Kubernetes Engine: Use Container Manager instead of Hypervisors. easy to add and remove resources by command. monitors the health of servers in the cluster and automatically repairs problems, such as failed servers. Support autoscale

	c. App Engine: Less configuration, focus on code with Java, Nodejs, Python, Go -> serverless app. 2 types: **standard** and **flexible**. Standard: No need to install additional system packages. Flexible: Run Docker container in App Engine environment, can install more packages.

	d. Cloud Function: lightweight computing option that is well suited to event-driven processing. must be short-running—this computing service is not designed to execute long-running code. Suite for call third-party services

### Storage Components of GCP
#### 1. Storage Resources
* Cloud Storage:
	- object storage system, is not a file system. It receives, stores, and retrieves files or objects from a distributed storage system.
	- useful for storing objects that are treated as single units of data. (an image)
	- extended periods of time but is rarely accessed => nearline storage
	- less than 1 years, inffrequent access => cold storage class.
* Persistent Disk:
	- is attacted to VMs
	- Support multiple readers without a degradation in performance. Multiple instances read a single copy of data. Can resized while in use without restart VM. Up to 64TB

* Cloud Storage for Firebase
	- Suit for mobile app, support up/download from mobile with unreliable network connections.

* Cloud Firestore
	- a shared file system for use with Compute Engine and Kubernetes Engine. NFS

#### 2. Database
* CLoud SQL:
	- Support Mysql, PostgresSQL.
	- First generation mysql sp: 16GB RAM, 500GB datastorage. Second generation sp: 416GB RAM, 10TB data storage, can configure automaticlly add storage as needed.
* Cloud Bigtable:
	- Designed for petabyte-scale app. Suite for app require low-latency write and read operations.
* Cloud Spanners:
	- Globally distributed relational database: strong consistency and transaction (Relation DB) + ability to scale horizontally like NoSQL
	- High availability, support encryption at rest and encryption in transit
	- Support ANSI 2011 standard SQL

* Cloud Datastore:
	- No SQL, flexible schema
	- Scale automatically. shard, partition. It takes care of replication, backups and other db admin tasks.
	- Support transactions, indexes and SQL-like queries.
	- Suite for app which need scale, structed data, do not always need strong consistency when reading data.

* Cloud Memorystore
	- In memory cache services
* Cloud Firestore
	- NoSQL, highly scalable web and mobile application
	- Provide offline support, sync, manage data across mobile devices, IoT devices, and backend data stores.

### Networking Components of GCP
#### 1. Networking Services
Help configure virtual networks within Google’s global network infrastructure, link on- premise data centers to Google’s network, optimize content delivery, and protect your cloud resources using network security services.

* Virtual Private Cloud:
	- controls what is physically located in that data center and connected to its network.
	- each enterprise can logically isolate its cloud resources by creating a virtual private cloud
	- Can access other services without public IP
	- Can linked to on-premise VPN using IPSec
	- VPC is Global, can use Firewall to restrict access to resources.
* Cloud Load Balancing:
	- distribute workloads across your cloud infra- structure.
	- is a software service that can load-balance HTTP, HTTPS, TCP/ SSL, and UDP traffic.
* Cloud Armor
	- network security service that builds on the Global HTTP(s) Load Balancing service.
	- Allow/Restrict IP. Counter Cross-site attacks. counter SQL injection attacks. Define rules at level 3 (network), level 7 (applicaiton). Restrict access based geolocation of incomming traffic.
* Cloud CDN:
	- enable low-latency response to these requests by caching content on a set of endpoints across the globe.
* Cloud Interconnect
	- connecting your existing networks to the Google network. Cloud Interconnect offers two types of connections: **interconnects** and **peering**.
* Cloud DNS
	-  a domain name service provided in GCP.

#### 2. Identity Management
GCP’s Cloud Identity and Access Management (IAM) service enables customers to define fine-grained access controls on resources in the cloud. IAM uses the concepts of users, roles, and privileges.

### Additional Components of GCP
#### 1. Management Tools
* Stackdriver: Collect metrics, logs, event data -> monitor, assess
* Monitoring: Collect performance data from GCP, AWS ... ngnix, cassandra, ES, ..
* Logging: Store and analyze, alert on log data from both GCP and AWS logs.
* Error Reporting: Report crash information
* Trace: Capture latency data -> identify performance problems.
* Debugger + Profiler.

#### 2. Specialized Services
* Apigee API Platform
* Data Analytics: BigQuery, Cloud Dataflow, Cloud Dataproc (managed Hadoop & Spark serivice), Cloud Dataprep (analysts to explore and prepare data for analystic)

#### 3. AI and Machine Learning
* Cloud AutoML: develop machine learning models without ML exp
* CLoud ML Engine: dev + deploy scalable ML system to production
* Cloud Natureal Language Processing: analyze human languages and extracting information from text
* CLoud Vision: Analysis images with metadata, text, filtering content.

## Chapter 3. Projects, Service Accounts, and Billing

### How GCP Organizes Projects and Accounts
GCP provides a way to group resources and manage them as a single unit. This is called the *resource hierarchy*. The access to resources in the resource hierarchy is controlled by a set of **policies** that you can define.
#### 1. GCP Resource Hierarchy
* Organization
	- Is the root of the resource hierarchy. ~ company/ organization.
	- Use G-suite domains + Cloud Identity account.
	- Have super admins and they will assign role to other users (Organization Administrator IAM role)
* Folder
	- The building blocks of multilayer organizational hierarchies.
	- May contain both folder and project
* Project
	- It is in projects that we create resources, use GCP services, manage permissions, and manage billing options.

#### 2. Organization Policies
-  Organization Policy Service: controls access to an organi- zation’s resources.
-  IAM specifies who can do things, and the Organization Policy Service specifies what can be done with resources.

* Contraints on Resources
	- Constraints are restrictions on services
	- **List constraints** are lists of values that are allowed or disallowed for a resource.
	- **Boolean constrains** evaluate to true or false and determine whether the constraint is applied or not.

* Policy Evaluation
	- Policies are managed through the Organization Policies form in the IAM & admin form
	- Multiple policies can be in effect for a folder or project.

### Roles and Identities
#### 1. Roles in GCP
- A role is a collection of permissions. Roles are granted to users by binding a user to a role. **Identities** - human user or service account.
- There are 3 types of roles:
	- Primitive roles: Owner, Editor and Viewer
	- Predefined roles
	- Custom roles

- Need to follow *principle of least privilege*
- Custom roles are assembled using permissions defined in IAM.

#### 2. Granting Roles to Identities
- Use Console to granting role

### Service Accounts
- Identities associated with individual users. Sometimes it helpful have appliation or VMs act on behalf of a user or perform operations that the user does not have permission to perform.
- 2 types of service accounts, user-managed service accounts and Google- managed service accounts.

### Billing
Using resources such as VMs, object storage, and specialized services usually incurs charges.
#### 1. Billing Accounts

Billing accounts store information about how to pay charges for resources used. A billing account is associated with one or more projects. All projects must have a billing account unless they use only free services.

* two types of billing accounts: self-serve and invoiced. Self-serve accounts are paid by credit card or direct debit from a bank account. The other type is an invoiced billing account, in which bills or invoices are sent to customers.

* Billing roles:
	* Billing Account Creator, which can create new self-service billing accounts
	* Billing Account Administrator, which manages billing accounts but cannot create them.
	* Billing Account User, which enables a user to link projects to billing accounts
	* Billing Account Viewer, which enables a user to view billing account cost and transactions

#### 2. Billing Budgets and Alerts
Defining a budget and setting billing alerts.

One or more projects can be linked to a billing account, so the budget and alerts you specify should be based on what you expect to spend for all projects linked to the billing account.
#### 3. Exporting Billing Data
Can use Billing Export or BigQuery

### Provisioning Stackdriver Workspaces
Create a Stackdriver Workspaces.

Stackdriver is a set of services for monitoring, logging, tracing, and debugging applications and resources

## Chapter 4. Introduction to Computing in Google Cloud
### Compute Engine
Compute Engine is a service that provides VMs - *instance*. When you use Compute Engine, you create and manage one or more instances.
#### 1. Virtual Machine Images
Instances run images, which contain operating systems, libraries, and other code. If there is no public image that meets your needs, you can create a custom image from a boot disk or by starting with another image. After that, you can create a snapshot.

Custom images are especially useful if you have to configure an operating system and install additional software on each instance of a VM that you run.

Useful when we want to config system, install additional software. Install 1, start VM with this image in boosting.
#### 2. Virtual Machines Are Contained in Projects
When you create an instance, you specify a project to contain the instance.
#### 3. Virtual Machines Run in a Zone and Region
You specify a region and a zone when you create a VM.

When we select zone for our VMs, consider:

* Cost, which can vary between regions.
* Data locality regulations: Put VMs near your customer
* High availability: Put VMs in multiple zones/region
* Latency
* Need for specific hardware platforms, which can vary by region.

#### 4. Users Need Privileges to Create Virtual Machines
Users can be associated with projects as follows: Individual users, A Google group, A G-Suite domain, A service account

* **Compute Engine Admin**:full control over Compute Engine instances.
* **Compute Engine Network Admin**: create, modify, and delete most networking resources,read-only access to firewall rules and SSL certifications, does not give the user permission to create or alter instances.
* **Compute Engine Security Admin**: create, modify, and delete SSL certificates and firewall rules.
* **Compute Engine Viewer** get and list Compute Engine resources but cannot read data from those resources.

We could grant permissions is to attach IAM policies directly to resources. (A for VM1 and B for VM2)
#### 5. Preemptible Virtual Machines
Preemptible VMs are short-lived compute instances suitable for running certain types of workloads— particularly for applications that perform financial modeling, rendering, big data, continuous integration, and web crawling operations. persist for up to 24 hours. help reduce cost

Limitation:

* May terminate at any time. If they terminate within 10 minutes of starting, you will not be charged for that time.
* Will be terminated within 24 hours.
* May not always be available. Availability may vary across zones and regions.
* Cannot migrate to a regular VM.
* Cannot be set to automatically restart.
* Are not covered by any service level agreement (SLA).
#### 6. Custom Machine Types
Compute Engine has more than 25 predefined machine types grouped into standard types, high-memory machines, high-CPU machines, shared core type, and memory-optimized machines.

You can create a custom Machine Type. It can have between 1 and 64 vCPUs and up to 6.5GB of memory per vCPU. The price of a custom configuration is based on the number of vCPUs and the memory allocated.

#### 7. Use Cases for Compute Engine Virtual Machines
Use when you need maximum control over VM instances:

* Choose the specific image to run on the instance.
* Install software packages or custom libraries.
* Have fine-grained control over which users have permissions on the instance.
* Have control over SSL certificates and firewall rules for the instance

=> We need config to choose image, number of CPUs, memory, storage, network,...  The more control over a resource you have in GCP, the more responsibility you have to configure and manage the resource.

### App Engine
App Engine is a PaaS compute service that provides a managed platform for running appli- cations, allow us focus on application rather config VMs
#### 1. Structure of an App Engine Application
Have a common structure, and they consist of services, have versions, allow multiple versions run at one time. Each version of a service runs on an instance that is managed by App Engine.

The number of instances depends on **your configuration** for the application and the **current load** on the application.

Add instances to meet the need, and shut down when traffic decrease => **dynamic instances**.

App Engine also provides **resident instances**. These instances run continually. You can add or remove resident instances manually.

To estimate cost of running instance, GCP allow setup daily spending limits as well as create budgets and set alarms.
#### 2. App Engine Standard and Flexible Environments
* **App Engine Standard Environment**:
	* consists of a precon- figured, language-specific runtime.
	* Support for Java 8, Python 3.7, PHP 7.2, Nodejs 8, Go 1.11
* **App Engine Flexible Environment**:
	* Have no language and customization constraints.
	* Uses containers as the basic building block abstraction. Can customize by container configuration.
	* Quite same Kubernetes, but App Engine flexible env provide fully managed PaaS and is a good option when you can package your application and services into a small set of containers, can be autoscales. Kubernetes needs more configuration and monitoring by yourself.

#### 3. Use Cases for App Engine
* Good choice for a computing platform when you have little need to configure and control the underlying operating system or storage system.
* The App Engine standard environment is designed for applications written in one of the supported languages.
* The App Engine flexible environment is well suited for applications that can be decomposed into services and where each service can be containerized. If you need to install additional software or run com- mands during startup, you can specify those in the Dockerfile.

### Kubernetes Engine
Kubernetes is an open source tool created by Google for administering clusters of virtual and bare-metal machines. Kubernetes is a container orchestration service that helps you: Create cluster, deploy app, administer the cluster, specify policies and monitor cluster health.

Kubernetes ~ *instance group* of Compute Engine?
#### 1. Kubernetes Functionality
* Load balancing across Compute Engine VMs that are deployed in a Kubernetes cluster
* Automatic scaling of nodes (VMs) in the cluster
* Automatic upgrading of cluster software as needed
* Node monitoring and health repair
* Logging
* Support for node pools, which are collections of nodes all with the same configuration

#### 2. Kubernetes Cluster Architecture
A cluster master node and one or more worker nodes ~ *master* and *nodes*

The master determines what containers and workloads are run on each node.

Nodes are Compute Engine VMs. Kubernetes deploys containers in groups called *pods*. Containers within a single pod share storage and network resources. Containers within a pod share an IP address and port space. A pod is a logically single unit for providing a service.

#### 3. Kubernetes High Availability
* First way: *eviction policies* that set thresholds for resources. When they meet thresholds -> start shutting down pods

* Second way: multiple identical pods. Group of running identical pods are *deployments*. Identical pods as *replicas*

#### 4. Kubernetes Engine Use Cases
A good choice for large-scale applications that require high availabil- ity and high reliability.

For example: If you have a set of services that support a user interface, another set that implements business logic, and a third set that provides backend services. Each of these different groups of services can have different lifecycles and scalability requirements
### Cloud Functions
A serverless computing platform designed to run single-purpose pieces of code in response to events in the GCP environment.

#### 1. Cloud Functions Execution Environment
* The functions execute in a secure, isolated execution environment.
* Compute resources scale as needed to run as many instances of Cloud Functions as needed without you having to do anything to control scaling.
* The execution of one function is independent of all others. The lifecycles of Cloud Functions are not dependent on each other. => stateless
#### 2. Cloud Functions Use Cases
Suited to short-running, event-based processing.

## Chapter 5. Computing with Compute Engine Virtual Machines
### Creating and Configuring Virtual Machines with the Console
Need to enable Billing
#### 1. Main Virtual Machine Configuration Details
+ Name, Region and zone, Machine type (CPUs/Memory), Boot disk (OS), Service Account

#### 2. Additional Configuration Details
* Management Tab:
	* Label: key-value, help to understand how VM is used.
	* Deletion protection
	* Startup script
	* Metadata (maybe `startup-script-url`)
	* Availability Policy: Preemptibility, Automatic restart, On host maintenance
* Security Tab:
	* Shielded VMs: Secure Boot, Virtual Trusted Platform Module, Integrity Monitoring
	* SSH Key
* Disk:
	* Boot Disk: Config delete boot disk when instance is deleted.
	* Encryption data: by Google/Customer-managed key/Customer supplied
* Networking:
	* Network tags (Can assign tags, firewall will work with this tag)
	* Network interface
* Sole Tenancy tab:
	* Allows you to specify labels regarding sole tenancy for the server (???)

### Creating and Configuring Virtual Machines with Cloud SDK

### Basic Virtual Machine Management
#### 1. Starting and Stopping Instances
`gcloud compute instances stop INSTANCE-NAME`
#### 2. Network Access to Virtual Machines
Use `SSH` or `RDP`
#### 3. Monitoring a Virtual Machine
View in Console Instance detail page
#### 4. Cost of Virtual Machines
* VMs are billed in 1-second increments.
* The cost is based on machine type. The more CPUs and memory used, the higher the cost.
* Google offers discounts for sustained usage.
* VMs are charged for a minimum of 1 minute of use.
* Preemptible VMs can save you up to 80 percent of the cost of a VM.

### Guidelines for Planning, Deploying, and Managing Virtual
* Choose a machine type with the fewest CPUs and the smallest amount of memory that still meets your requirements, including peak capacity. This will minimize the cost of the VM.
* Use the console for ad hoc administration of VMs. Use scripts with gcloud commands for tasks that will be repeated.
* Use startup scripts to perform software updates and other tasks that should be per- formed on startup.
* If you make many modifications to a machine image, consider saving it and using it with new instances rather than running the same set of modifications on every new instance.
* If you can tolerate unplanned disruptions, use preemptible VMs to reduce cost.
* Use SSH or RDP to access a VM to perform operating system–level tasks.
* Use Cloud Console, Cloud Shell, or Cloud SDK to perform VM-level tasks.

## Chapter 6. Managing Virtual Machines
### Managing Single Virtual Machine Instances
**Single instance** - one created by itself and not in an instance group or other type of cluster.
#### 1. Managing Single Virtual Machine Instances in the Console
* Starting, Stopping, and Deleting Instances
	* Reset command restarts a VM. The properties of the VM will not change, but data in memory will be lost. If you want to keep data, just save it on persistent disk or Cloud Storage.
* Viewing Virtual Machine Inventory
	* We can filter by instance name, label, internal ip, external ip, status, zone, network, ..
* Attaching GPUs to an Instance:
	* Start instance in which GPU libraries have been installed or will be installed. (Choose boot disk)
	* Must also verify that the instance will run in a zone that has GPUs available.
	* Custom Machine type, config number of GPUs to attach
	*  The CPU must be compatible with the GPU selected. GPUs cannot be attached to shared memory machines.
	*  If you add GPUs, you must set the instance to terminate during maintenance.
* Working with Snapshots:
	* Snapshots are copies of data on a persistent disk.
	* If you are running a database or other application that may buffer data in memory before writing to disk, be sure to flush disk buffers before you create the snapshot; other- wise, data in memory that should be written to disk may be lost
	* Need **Compute Storage Admin role**
* Working with Images:
	* Similar to snapshots in that they are copies of disk contents. The difference is that snapshots are used to make data available on a disk, while images are used to create VMs.
	* Can create from Disk, Snapshot, Cloud storage file, Another image.
	* Delete removes the image, while Deprecated marks the image as no longer supported and allows you to specify a replacement image to use going forward.

#### 2. Managing a Single Virtual Machine Instance with Cloud Shell and the Command Line
* Gcloud global flags: `--account`, `--configuration`, `--flatten`, `--format`, `--help`, `--project`, `--quiet`, `--verbosity` (debug/warning/info/error)

```sh
# Start instance
gcloud compute instances start INSTANCE_NAMES --async --zone us-central1-c

# Stop instances
gcloud compute instances stop INSTANCE_NAMES

# Delete instances
gcloud compute instances delete INSTANCE_NAMES --zone us-central2-b (may be add option --keep-disks=all  | --delete-disks=data)

# View VM inventory
gcloud compute instances list --filter="zone:ZONE" (--sort-by | --limit)

# Create Snapshot of a disk
gcloud compute disks snapshot DISK_NAME --snapshot-names=NAME
gcloud compute snapshots describe SNAPSHOT_NAME

# To create a disk
gcloud compute disks create DISK_NAME --source-snapshot=SNAPSHOT_NAME --size=100 --type=pd-standard

# Create Image
gcloud compute images create IMAGE_NAME (--source-disk | --source-image | --source-image-family | --source-snapshot | --source-uri | --description | --labels)
gcloud compute images delete IMAGE_NAME

# Export to Cloud storage
gcloud compute images export --destination-uri DESTINATION_URI --image IMAGE_NAME
```

### Introduction to Instance Groups
* **Managed groups** consist of groups of identical VMs, are created using an instance template, can automatically scale the number of instances in a group and be used with load balancing to distribute workloads
* **Unmanaged groups** should be used only when you need to work with different configu- rations within different VMs within the group.
#### 1. Creating and Removing Instance Groups and Templates

```sh
# Create instance template
gcloud compute instance-templates create INSTANCE
gcloud compute instance-templates create ch06-instance-template-1 --source- instance=ch06-instance-1

# Delete instance template
gcloud compute instance-templates delete NAME

# Delete instance group
gcloud compute instance-groups managed delete-instances NAME

gcloud compute instance-templates list
gcloud compute instance-groups managed list-instances
gcloud compute instance-groups managed list-instances INSTANCE-GROUP-NAME
```
#### 2. Instance Groups Load Balancing and Autoscaling
Managed instance groups can be configured to autoscale with policy to trigger adding or removing instances based on CPU utilization, monitoring metric, load-balancing capacity, or queue-based workloads.
### Guidelines for Managing Virtual Machines
* Use labels and descriptions. This will help you identify the purpose of an instance and also help when filtering lists of instances.
* Use managed instance groups to enable autoscaling and load balancing. These are key
to deploying scalable and highly available services.
* Use GPUs for numeric-intensive processing, such as machine learning and high-performance computing. For some applications, GPUs can give greater performance benefit than adding another CPU.
* Use snapshots to save the state of a disk or to make copies. These can be saved in Cloud Storage and act as backups.
* Use preemptible instances for workloads that can tolerate disruption. This will reduce the cost of the instance by up to 80 percent.

## Chapter 7. Computing with Kubernetes
### Introduction to Kubernetes Engine
Kubernetes Engine is GCP managed Kubernetes service, for creating + maintaining Kubernetes cluster without having to manage Kubernetes platform.

Kubernetes runs containers on a cluster of VMs: where to run, monitors the health, and manages lifecycle of VM instances. This collection of tasks is known as *container orchestration*.

Instance group is quite similar, but more restricted. All instances run the same image and it has no mechanism to support the deployment of containers.

Keep in mind: when you use Kubernetes Engine, you will **manage Kubernetes** and **your applications** and **workloads running in containers** on the Kubernetes platform.

#### 1. Kubernetes Cluster Architecture
+ Cluster master and one or more nodes. Cluster master can be replicated and distributed for high-availability and fault tolerance.
+ The cluster master manages services: Kubernetes API, controllers, and schedulers.
+ Nodes are VMs that run containers configured to run an application. The nodes run an agent called **kubelet**, which is the service that communicates with the cluster master.

![](https://platform9.com/wp-content/uploads/2019/05/kubernetes-constructs-concepts-architecture.jpg)

#### 2. Kubernetes Objects
* **Pods**:
	* Pods are single instances of a running process in a cluster. Pods contain at least one container.
	* Each pod gets a unique IP address and a set of ports. Containers connect to a port.
	* A pod allows its containers to behave as if they are running on an isolated VM, sharing common storage, one IP address, and a set of ports. => can deploy multiple instance of the same application, or different instances of different applica- tions on the same node or different nodes
	* Pods support autoscaling. The mechanism that manages scaling and health monitoring is known as a **controller**.
	* Quite same Compute Engine manage instance group. But Pods is manage automaticly by controller, and it excutes application on containers.
	* **Pods are ephemeral and can be terminated by a controller**.

* **Services**:
	* Cause pods are ephemeral => We can't depend on Pods to comunicate with applications (EX: Pods IP Address)
	* K8s provides a level of indirection between applications running in pods and other applications: *service* - provide API endpoints
* **ReplicaSet**:
	* A ReplicaSet is a controller used by a deployment that ensures the correct number identical of pods are running. (detect enough pods running for an application, and create/delete)
* **Deployment**:
	* Deployments are sets of identical pods, running same application, which are created using the same pod template.
	* A pod template is a definition of how to run a pod - *pod specification*
	* Suited to stateless applications
* **StatefulSet**:
	* StatefulSets are like deployments, but they assign unique identifiers to pods.
	* Used when an application needs a unique network identifier or stable persistent storage.
* **Job**:
	* A job is an abstraction about a workload.
	* Job specifications are specified in a configuration file and include specifications about the container to use and what command to run.

### Deploying Kubernetes Clusters
#### 1. Deploying Kubernetes Clusters Using Cloud Console
#### 2. Deploying Kubernetes Clusters Using Cloud Shell and Cloud SDK

```sh
gcloud beta container

gcloud beta container --project "ferrous-depth-220417" clusters create "standard-cluster-2" --zone "us-central1-a" --username "admin"
--cluster-version "1.9.7-gke.6" --machine-type "n1-standard-1"
--image-type "COS" --disk-type "pd-standard" --disk-size "100" --scopes "https://www.googleapis.com/auth/compute","https://www.googleapis.com/auth/ devstorage.read_only","https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/ servicecontrol","https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-cloud-logging --enable-cloud-monitoring --network "projects/ferrous-depth-220417/ global/networks/default" --subnetwork "projects/ferrous-depth-220417/regions/ us-central1/subnetworks/default" --addons HorizontalPodAutoscaling, HttpLoadBalancing,KubernetesDashboard --enable-autoupgrade --enable-autorepair
```

### Deploying Application Pods
* Create a deployment: Container image, Environment variables, Initial command,Application name, Labels, Namespace, Cluster to deploy to

```sh
gcloud components install kubectl

# Run Docker image on a cluster
kubectl run ch07-app-deploy --image=ch07-app --port=8080

# Scale up
kubectl scale deployment ch07-app-deploy --replicas=5
```
### Monitoring Kubernetes
Enable Stackdriver monitoring and logging and send notifications.

## Chapter 8. Manage Kubernetes Clusters


### Viewing the Status of a Kubernetes Cluster
#### 1. View on console
* Detail
	* The Add-ons section displays the status of optional add-on features of a cluster. The Permissions section shows which GCP service APIs are enabled for the cluster.
	* Node pools, which are separate instance groups running in a Kubernetes clusters.
* Storage
	* Cluster does not have persistent volumes but uses standard storage.
* Nodes

#### 2. Cloud Shell
* Use `gcloud` command for getting status of cluster
* Use `kubectl` command for getting info about Kubernetes managed objects (nodes, pods, containers)

```sh
# List name and basic info of all clusters
gcloud container clusters list

# View detail of a cluster
gcloud container clusters describe --zone us-central1-a standard-cluster-1

# Get kubeconfig content to connect with Kubernetes API
gcloud container clusters get-credentials --zone us-central1-a standard-cluster-1

# Get nodes/pods
kubectl get nodes
kubectl get pods
kubectl describe nodes
kubectl describe pods
```


Fun fact: "You might expect the Kubernetes Engine commands to start with `gcloud kubernetes`, but the service was originally called Google Container Engine. In November 2017, Google renamed the service Kubernetes Engine, but the gcloud commands remained the same."

### Adding, Modifying, and Removing Nodes

```sh
# Add or modify nodes - Change size to 5
gcloud container clusters resize standard-cluster-1 --node-pool default-pool --size 5 --region=us-central1

# Modify cluster, update autoscaling
gcloud container clusters update standard-cluster-1 --enable-autoscaling --min-nodes 1 \
--max-nodes 5 --zone us-central1-a --node-pool default-pool

```

### Adding, Modifying, and Removing Pods
It is considered a best practice to not manipulate pods directly. Kubernetes will maintain the number of pods specified for a deployment. If you would like to change the number of pods, you should change the deployment configuration.

Pods are managed through deployments. A deployment includes a configuration parameter called *replicas*, which are the number of pods running the application specified in the deployment.

```sh
# List deployments
kubectl get deployments

# Change the replicas to 5
kubectl scale deployment nginx-1 --replicas 5

# Autoscale: add or remove pods as needed to meet demand based on CPU utilization
kubectl autoscale deployment nginx-1 --max 10 --min 1 --cpu-percent 80

# Remove a deployment
kubectl delete deployment nginx-1
```

### Adding, Modifying, and Removing Services
Services are added through deployments.

```sh
# Kuber list services
kubectl get services

# Kuber add service
kubectl run hello-server --image=gcr.io/google/samples/hello-app:1.0 --port 8080

# Service need to expose port, use this command
kubectl expose deployment hello-server --type="LoadBalancer"

# Delete service
kubectl delete service hello-server
```
### Viewing the Image Repository and Image Details

```sh
# View list images in registry
gcloud container images list

gcloud container images list --repository gcr.io/google-containers

# View image detail
gcloud container images describe gcr.io/appengflex-project-1/nginx
```

## Chapter 9. Computing with App Engine
### App Engine Components
* App Engine Standard applications consist of four components:
	* Application
	* Service
	* Version
	* Instance
* All resources associated will be created in the same region with application.
* App have multiple services, Services can have multiple versions. When a version executes, it creates an instance of the app.
* Services are defined by their source code and their configuration file. The combination of those files constitutes a version of the app. => easy for rolling back, easy for spliting traffic.

![](https://cloud.google.com/appengine/docs/images/modules_hierarchy.svg?hl=zh-cn)

### Deploying an App Engine Application

```sh
gcloud app deploy app.yml

# Addition options: --version - specific version; --project, --no-promote - Deploy app without routing traffic to it

# Stop serving versions
gcloud app versions stop v1 v2

```
### Scaling App Engine Applications
* `dynamic` instances and `resident` instances.
* To specify automatic scaling, add config options: `target_cpu_utilization`, `target_throughput_utilization`, `max_concurrent_requests`, `max_instances`, `min_instances`, `max_pending_latency`, `min_pending_latency`.
* Basic scaling: `idle_timeout` and `max_instances`.
* Manual scaling: `manual_scaling: instances: 7`

### Splitting Traffic between App Engine Versions
* If you have more than one version of an application running, you can split traffic between the versions
* Three ways to split traffic:
	* IP address: splitting provides some stickiness, so a client is always routed to the same split
	* HTTP cookie: useful when you want to assign users to versions (request header: `GOOGAPPUID`)
	* Random Selection: useful when you want to evenly distribute workload.

```sh
# Command to split traffic
# --migrate: should migrate traffic from pervious version to new version
# --split-by specifies how to split traffic using either IP or cookies: ip, cookie or random.
gcloud app services set-traffic serv1 --splits v1=.4,v2=.6
```

## Chapter 10. Computing with Cloud Functions
### Introduction to Cloud Functions
Cloud Functions is a **serverless** compute service provided by Google Cloud Platform (GCP).

App Engine supports multiple services organized into a single application, while Cloud Functions supports individual services that are managed and operate independently of other services.

Cloud Functions allows developers to decouple the initial data quality check from the rest of the extraction, transformation, and load process.
#### 1. Events, Triggers, and Functions
* **Events** are a particular action that happens in Google Cloud
	* Cloud Storage Cloud: uploading, deleting, and archiving a file.
	* Pub/Sub: an event for publishing a message
	* HTTP type of event allows developers to invoke a function by making an HTTP request using POST, GET, PUT, DELETE, and OPTIONS calls.
	* Firebase: actions taken in the Firebase database, such as database triggers, remote configuration triggers, and authentication triggers.
	* Stackdriver Logging: a change

* A **trigger** is a way of responding to an event.
* The **function** is passed arguments with data about the event.
#### 2. Runtime Environments
* Functions run **in their own environment**. (separate instance). We can't share information between invocation of functions. If we wanna keep data, just use database (Cloud Datastore/ file in Cloud Storage)
* Support Python 3, Node 6, Node 8
### Cloud Functions Receiving Events from Cloud Storage
* Function name
* Memory allocated for the function - from 128MB to 2GB (default 256MB)
* Trigger
* Event type
* Source of the function code
* Runtime
* Source code
* Python, Go or Node.js function to execute


`gcloud function deploy` need: runtime, trigger-resource, trigger-event.

trigger-event (google.storage.object.finalize, google.storage.object.delete, google.storage.object.archive, google.storage.object.metadataUpdate)

```sh
gcloud functions deploy FUNCTION_NAME --runtime python37 --trigger-resource BUCKET_NAME --trigger-event EVENT_NAME

gcloud functions delete cloud_storage_function_test
```
### Cloud Functions Receiving Events from Pub/Sub
Parameter:

* Cloud function name
* Memory allocated for the function
* Trigger
* Topic
* Source of the function code
* Runtime
* Source code
* Name of the Python or Node.js function to execute

```sh
gcloud functions deploy pub_sub_function_test --runtime python37 --trigger-topic gcp-ace-exam-test-topic
```

Timeout of a Cloud Function is 1 minutes by default. You can add option `timeout` to command, max to 9 minutes.


## Chapter 11. Planning Storage in the Cloud

## Chapter 12. Deploying Storage in Google Cloud Platform

## Chapter 13. Loading Data into Storage

## Chapter 14. Networking in the Cloud: Virtual Private Clouds and Virtual Private Networks

## Chapter 15. Networking in the Cloud: DNS, Load Balancing, and IP Addressing

## Chapter 16. Deploying Applications with Cloud Launcher and Deployment Manager

## Chapter 17. Configuring Access and Security

## Chapter 18. Monitoring, Logging, and Cost Estimating

