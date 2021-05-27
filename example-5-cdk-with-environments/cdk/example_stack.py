from aws_cdk import aws_s3, core


class ExampleStack(core.Stack):
    def __init__(
        self, scope: core.Construct, construct_id: str, identifier: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = aws_s3.Bucket(
            self,
            id=f"message-bucket-{identifier}",
            access_control=aws_s3.BucketAccessControl.PUBLIC_READ,
            public_read_access=True,
            auto_delete_objects=True,
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        core.CfnOutput(
            self, id=f"message-bucket-name-{identifier}", value=bucket.bucket_name
        )

        core.CfnOutput(
            self,
            id=f"message-bucket-url-{identifier}",
            value=f"https://{bucket.bucket_domain_name}",
        )
