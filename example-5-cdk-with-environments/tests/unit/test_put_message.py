from assertpy import assert_that

from src.put_message import put_message


def test_that_put_message_correctly_populates_file_in_s3(
    expected_file_contents, mock_bucket, mock_s3_resource
):
    put_message("Test", mock_bucket.name)

    assert_that(list(mock_bucket.objects.all())).is_length(1)

    message = mock_s3_resource.Object(bucket_name=mock_bucket.name, key="message.html")

    message_body = message.get()["Body"].read().decode("utf-8")

    assert_that(message_body).is_equal_to(expected_file_contents)
