# DynamoDB

DynamoDB is a fast, fully managed NoSQL database service that makes it simple and cost-effective to store and retrieve any amount of data, and serve any level of request traffic. Its guaranteed throughput and single-digit millisecond latency make it a great fit for gaming, ad tech, mobile and many other applications.

Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance.

* Query: Searche only primary key attribute values and supports a subset of
    comparision operators on key attribute values to refine the search process

* Scan: Scan the entire table. You ca specify filters to apply to the results to
    refine the values returned to you, after the complete scan.

Setting IAM with condition:
```json
"ForAllValues:StringEquals": {
    "dynamodb:Attributes": [
        "SuperHero",
        "MissionStatus",
        "Villain1",
        "Villain2",
        "Villain3"
    ]
}
```

allow users or entity that assumes the role to perform a Query operation, but only against the specified attributes. This powerful feature enables you to implement column-level security on your DynamoDB tables.
