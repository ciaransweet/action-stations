import os
from pytest import fixture


@fixture
def deployed_message_url():
    return os.environ["DEPLOYED_MESSAGE_URL"]


@fixture
def expected_file_contents() -> str:
    return f"""
<h1>Hello there!</h1>

You are seeing this message in the "{os.environ['IDENTIFIER']}" Environment<br>

The secret is: "{os.environ['SECRET']}"
"""
