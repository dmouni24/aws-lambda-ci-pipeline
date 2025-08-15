# AWS Lambda CI Pipeline: Log Validation Tool

Python-based CLI tool that validates logs from AWS S3 and CloudWatch, designed for QA automation in CI/CD pipelines.

## 📌 Features
- Triggered via AWS Lambda or CLI
- Reads logs from AWS S3 or CloudWatch
- Validates patterns (e.g., errors, warnings)
- JSON and text log support
- CI-ready with test coverage

## 🛠 Tech Stack
- Python 3.x
- Boto3
- AWS Lambda
- CloudWatch Logs
- AWS S3
- PyTest

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python cli/validator.py --source s3 --bucket my-bucket --pattern "ERROR"
```

