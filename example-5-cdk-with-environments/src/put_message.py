import json
import sys
from typing import Dict

import boto3


def get_stack_outputs(stack_output_path: str) -> Dict:
    with open(stack_output_path, "r") as stack_output_file:
        return json.load(stack_output_file)


def put_message(env: str, stack_output_path: str, secret: str) -> None:
    stack_outputs = get_stack_outputs(stack_output_path)
    bucket = stack_outputs[f"action-stations-example-5-{env}"][
        f"messagebucketname{env}"
    ]
    s3_client = boto3.client("s3")
    s3_client.put_object(
        ACL="public-read",
        Bucket=bucket,
        Key="message.html",
        ContentType="text/html",
        Body=f"""
<h1>Hello there!</h1>

You are seeing this message in the "{env}" Environment<br>

The secret is: "{secret}"
""",
    )
    bucket_url = stack_outputs[f"action-stations-example-5-{env}"][
        f"messagebucketurl{env}"
    ]
    print(f"{bucket_url}/message.html")


if __name__ == "__main__":
    put_message(sys.argv[1], sys.argv[2], sys.argv[3])
