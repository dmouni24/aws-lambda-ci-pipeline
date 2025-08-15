import json
from cli.utils.aws_utils import fetch_logs_from_s3

def lambda_handler(event, context):
    bucket = event.get('bucket')
    pattern = event.get('pattern')
    logs = fetch_logs_from_s3(bucket)
    matched = [log for log in logs if pattern in log]
    return {
        'statusCode': 200,
        'matched_logs': matched,
        'count': len(matched)
    }
