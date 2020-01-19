# AWS Command Line Interface

The CLI could be used for activities such as:

* Sending backups to the cloud
* Providing shared access to documents from multiple computers
* Retrieving scripts and application code from a central repository
* Duplicating data between different regions

Instance metadata is data about your instance that you can use to configure or manage the running instance. Included in the data is a set of security credentials that was used for all your commands during this lab.

It works as follows:

A role called scripts was created with appropriate permissions to run the lab.
The Amazon EC2 instance you have been using was launched with the scripts role.
The AWS CLI and Python SDK automatically retrieved the security credentials via the Instance Metadata Service.
You can also view the security credentials by calling the Instance Metadata Service.

These SDKs make it easy for your own software to interact with AWS. They also automatically retrieve Security Credentials via the Instance Metadata Service when running on EC2 instances.
