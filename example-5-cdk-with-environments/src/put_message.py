import boto3


def put_message(message: str, bucket_name: str) -> None:
    s3_client = boto3.client("s3")
    s3_client.put_object(
        Bucket=bucket_name,
        Key="message.html",
        Body=f"""
<h1>Hello there!</h1>

You are seeing this message in the "{message}" Environment
"""
    )
