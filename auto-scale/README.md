# Auto Scale

- Auto Scale is a way to set "cloud temperature". Use policies to "set the thermostat", and Under the hood, AutoScaling controls the heat by adding and subtracting EC2 resources on an as-need basis in order to maintain the "temperature" (capacity). An Auto Scaling policy consists of:
  - A `launch configuration` that defines the servers that are created in response to increased demand.
  - An `Auto Scaling group` that defines when to use a launch configuration to create new server instances and in wich Availability Zone and load balancer context they should be created.

- AS assumes a set of homogeneous servers. That is, AS does not know that Server A is a 64 bit extra-large instance and more capable than a 32-bit small instance. This is a core tenet of cloud computing: scale horizontally using a fleet of fungible resources; individual resource are secondary to the fleet itself.
