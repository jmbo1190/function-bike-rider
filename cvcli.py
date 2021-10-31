#!/usr/bin/env python
import click

# import boto3
from labels import labels


@click.command()
@click.option(
    "--bucket",
    prompt="Pass in the S3 Bucket (e.g. cloud-comp-found-function-bike-rider)",
    help="This is the S3 Bucket",
)
@click.option(
    "--name",
    help="This is the name of the image",
    prompt="Pass in the name (e.g. lion.jpg)",
)
def calllabels(bucket, name):
    """CLI call to Computer Vision function labels() \n
    example usage: \n
       cvcli.py --help
       cvcli.py --bucket "cloud-comp-found-function-bike-rider" --name "Lion.jpg"\n
    """

    # print(f"This is the bucketname {bucket} !")
    # print(f"This is the imagename {name} !")
    found_labels = labels(bucket, name)
    click.echo(click.style("Found Labels:", fg="red"))
    for label in found_labels:
        click.echo(click.style(f"{label}", bg="blue", fg="white"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    calllabels()
