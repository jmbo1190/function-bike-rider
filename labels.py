import boto3


def labels(bucket, name):
    """This takes an S3 bucket and a image name
       and returns the list of labels identified by Amazon Rekognition
    e.g. (if resource is: s3://cloud-comp-found-function-bike-rider)
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
    return response["Labels"]
