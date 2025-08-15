import click
from utils.aws_utils import fetch_logs_from_s3, fetch_logs_from_cloudwatch

@click.command()
@click.option('--source', type=click.Choice(['s3', 'cloudwatch']), required=True)
@click.option('--bucket', type=str, help='S3 bucket name')
@click.option('--log-group', type=str, help='CloudWatch log group name')
@click.option('--pattern', type=str, required=True, help='Pattern to search for')
def validate_logs(source, bucket, log_group, pattern):
    if source == 's3':
        logs = fetch_logs_from_s3(bucket)
    else:
        logs = fetch_logs_from_cloudwatch(log_group)

    matched = [log for log in logs if pattern in log]
    print(f"Found {len(matched)} log entries matching pattern '{pattern}':")
    for m in matched:
        print(m)

if __name__ == '__main__':
    validate_logs()
