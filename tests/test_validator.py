from cli.utils.aws_utils import fetch_logs_from_s3

def test_log_parsing(monkeypatch):
    def mock_fetch_logs_from_s3(bucket_name):
        return ["INFO: Everything is fine", "ERROR: Something went wrong"]

    monkeypatch.setattr("cli.utils.aws_utils.fetch_logs_from_s3", mock_fetch_logs_from_s3)
    logs = fetch_logs_from_s3("dummy-bucket")
    assert any("ERROR" in log for log in logs)
