import boto3

def fetch_logs_from_s3(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    logs = []
    for obj in response.get('Contents', []):
        body = s3.get_object(Bucket=bucket_name, Key=obj['Key'])['Body'].read().decode()
        logs.extend(body.splitlines())
    return logs

def fetch_logs_from_cloudwatch(log_group_name):
    client = boto3.client('logs')
    streams = client.describe_log_streams(logGroupName=log_group_name)['logStreams']
    logs = []
    for stream in streams:
        events = client.get_log_events(logGroupName=log_group_name, logStreamName=stream['logStreamName'])['events']
        logs.extend([e['message'] for e in events])
    return logs
