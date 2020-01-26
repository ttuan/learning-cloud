# Amazon Machine Images
Amazon EC2 provides templates known as Amazon Machine Images (AMIs) that contain a software configuration (for example, an operating system, an application server, and applications). You use these templates to launch an instance, which is a copy of the AMI running as a virtual server in the cloud.

A Quick Start AMI is independent of the instance type.

An AMI is really just a template document that contains information telling EC2 what OS and application software to include on the root data volume of the instance it’s about to launch. There are four kinds of AMIs.

* Amazon Quick Start AMI
* AWS Marketplace AMI: official, production-ready images provided and supported by industry vendors like SAP and Cisco.
* Community AMIs (more than 100k images) created and maintained by independent vendors and are usually built to meet a specific need.
* Private AMI

A particular AMI will be available in only a single region. Keep this in mind as you plan your deployments: invoking the ID of an AMI in one region while working from within a differ- ent region will fail.
