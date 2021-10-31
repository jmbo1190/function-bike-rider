import boto3


def labels(bucket, name):
    """This takes an S3 bucket and a image name
    e.g. (resource is: s3://cloud-comp-found-function-bike-rider)
         bucket = "cloud-comp-found-function-bike-rider"
         name = "lion.jpg"

    """

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
    return labels
