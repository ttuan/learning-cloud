# Security Group

Amazon EC2 security groups are an important control for restricting access to your AWS infrastructure.

- Virtual firewall for intances, control inbound and outbound traffic. SG
    act at intance level, not subnet level (therefore, each intance in
    subnet can has different set of security groups.)


- If you dont want to open request from public ip, remove protocol + port =>
    0.0.0.0. It seems like docker compose, you dont map port to the real host.
    Other service will connect by using service_name. (for example, no need to map
    redis port 6379 to localhost, app service just connect using service name
    "redis")
