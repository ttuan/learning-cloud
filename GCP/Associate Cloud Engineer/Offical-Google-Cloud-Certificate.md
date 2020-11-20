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

## Chapter 4. Introduction of COmputing in Google Cloud

## Chapter 5. Computing with Compute Engine Virtual Machines

## Chapter 6. Managing Virtual Machines

## Chapter 7. Computing with Kubernetes

## Chapter 8. Managing Kubernetes Clusters

## Chapter 9. Computing with App Engine

## Chapter 10. Computing with Cloud Functions

## Chapter 11. Planning Storage in the Cloud

## Chapter 12. Deploying Storage in Google Cloud Platform

## Chapter 13. Loading Data into Storage

## Chapter 14. Networking in the Cloud: Virtual Private Clouds and Virtual Private Networks

## Chapter 15. Networking in the Cloud: DNS, Load Balancing, and IP Addressing

## Chapter 16. Deploying Applications with Cloud Launcher and Deployment Manager

## Chapter 17. Configuring Access and Security

## Chapter 18. Monitoring, Logging, and Cost Estimating

