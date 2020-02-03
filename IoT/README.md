# AWS Internet of Things

AWS Internet of Things (IoT) is a managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices. AWS IoT can support billions of devices and trillions of messages, and can process and route those messages to AWS endpoints and to other devices reliably and securely. With AWS IoT, your applications can keep track of and communicate with all your devices, all the time, even when they aren't connected.

AWS IoT provides secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the AWS cloud. This enables you to collect telemetry data from multiple devices and store and analyze the data. You can also create applications that enable your users to control these devices from their phones or tablets.

- uses a topic-based publish/subscribe pattern
- AWS IoT supports MQTT connections using X.509 certificates. (not all device support HTTP connection)



1. Create X.509 Certificates by using aws cli (in EC2 instance - The simulator app)
2. Create thing type (In IoT Core - HomeAutomation)
3. Create thing (Thermostat) - Thing names are case sensitive
4. Create policy for the Thing - Secure/Policy tab
5. Attach policy and Thing to the Certificate - In Secure/Certificate tab
6. Create IoT Rule (in Act tab) to send message from IoT to SNS

For more information: https://www.qwiklabs.com/focuses/8546?parent=catalog
