#!/usr/bin/env python
import click
import boto3


@click.command()
@click.option("--bucket", 
	prompt="Pass in the S3 Bucket (e.g. cloud-comp-found-function-bike-rider)", 
	help="This is the S3 Bucket")
@click.option(
    "--name",
    help="This is the name of the image",
    prompt="Pass in the name (e.g. lion.jpg)",
)
def labels(bucket, name):
    """This takes an S3 bucket and a image name"""

    print(f"This is the bucketname {bucket} !")
    print(f"This is the imagename {name} !")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": name,
            }
        },
    )
    labels = response["Labels"]
    click.echo(click.style("Found Labels:", fg="red"))
    for label in labels:
        click.echo(click.style(f"{label}", bg="blue", fg="white"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    labels()
