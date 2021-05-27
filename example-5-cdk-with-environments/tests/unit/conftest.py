import os

import boto3
from moto import mock_s3
from pytest import fixture


@fixture
def expected_file_contents() -> str:
    return """
<h1>Hello there!</h1>

You are seeing this message in the "tests" Environment<br>

The secret is: "a-secret"
"""


@fixture
def test_stack_outputs_path() -> str:
    return f"{os.path.dirname(os.path.abspath(__file__))}/test_stack_outputs.json"


@fixture
def mock_s3_resource():
    with mock_s3():
        yield boto3.resource("s3")


@fixture
def mock_bucket(mock_s3_resource):
    bucket = mock_s3_resource.Bucket("test-bucket")
    bucket.create()
    yield bucket
