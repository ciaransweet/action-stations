from unittest.mock import patch

from assertpy import assert_that

from src.put_message import put_message


def test_that_put_message_correctly_populates_file_in_s3_and_is_publicly_available(
    expected_file_contents, mock_bucket, mock_s3_resource, test_stack_outputs_path
):
    with patch("builtins.print") as mock_print:
        put_message("tests", test_stack_outputs_path, "a-secret")

    assert_that(list(mock_bucket.objects.all())).is_length(1)

    message = mock_s3_resource.Object(bucket_name=mock_bucket.name, key="message.html")

    message_body = message.get()["Body"].read().decode("utf-8")

    assert_that(message_body).is_equal_to(expected_file_contents)

    public_to_all = False

    for grant in message.Acl().grants:
        if grant["Grantee"]["Type"] == "Group":
            if (
                grant["Grantee"]["URI"]
                == "http://acs.amazonaws.com/groups/global/AllUsers"
            ):
                public_to_all = grant["Permission"] == "READ"

    assert_that(public_to_all).is_true()

    assert_that(
        mock_print.assert_called_once_with(
            "https://test-bucket.s3.amazonaws.com/message.html"
        )
    )
