import requests
from assertpy import assert_that


def test_that_put_message_correctly_setups_message(
    expected_file_contents, deployed_message_url
):
    resp = requests.get(deployed_message_url)
    assert_that(resp.text).is_equal_to(expected_file_contents)
