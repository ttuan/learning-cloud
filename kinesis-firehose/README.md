# Amazon Kinesis Firehose

Amazon Kinesis Firehose is a fully managed service that delivers real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon Elasticsearch Service and Amazon Redshift. With Firehose, you do not need to write any applications or manage any resources. You configure your data producers to send data to Firehose and it automatically delivers the data to the specified destination.

Create lambda function - pre-process data.
Create stream in kinesis. Config pre-process function is Lambda function. Config
to pass data after process to ElasticSearch (to view with Kibana). Config S3 to
store failed response.
