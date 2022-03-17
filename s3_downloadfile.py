import logging
import boto3
from botocore.exceptions import ClientError
import os
import json

AWS_REGION = 'us-west-2'
AWS_PROFILE = 'default'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)

s3_resource = boto3.resource("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

def download_file(file_name, bucket, object_name):
    """
    Download a file from a S3 bucket.
    """
    try:
        response = s3_resource.Bucket(bucket).download_file(object_name, file_name)
    except ClientError:
        logger.exception('Could not download file to S3 bucket.')
        raise
    else:
        return response


def main():
    """
    Main invocation function.
    """
    file_name = 'hands-on-cloud-download.txt'
    object_name = 'names.txt'
    bucket = 'hands-on-cloud-localstack-bucket'

    logger.info('Downloading file to S3 bucket in LocalStack...')
    s3 = download_file(file_name, bucket, object_name)
    logger.info('File downloaded from S3 bucket successfully.')


if __name__ == '__main__':
    main()
