import logging
import boto3
from botocore.exceptions import ClientError
import os
import json

ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

s3_client = boto3.client("s3",
                         endpoint_url=ENDPOINT_URL)

def download_file(bucket, object_name, file_name):
    """
    Download a file from a S3 bucket.
    """
    try:
        response = s3_client.download_file(bucket, object_name, file_name)
    except ClientError:
        logger.exception('Could not download file to S3 bucket.')
        raise
    else:
        return True

def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to a S3 bucket.
    """
    try:
        if object_name is None:
            object_name = os.path.basename(file_name)
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError:
        logger.exception('Could not upload file to S3 bucket.')
        raise
    else:
        return True


def main():
    """
    Main invocation function.
    """
    file_name = 'employees.json'
    object_name = 'employees-on-cloud.json'
    bucket = 'hands-on-cloud-localstack-bucket'
    logger.info('Uploading file to S3 bucket ...')
    response = upload_file(file_name, bucket, object_name)
    logger.info('File uploaded to S3 bucket successfully.')
    response = download_file(bucket, object_name, object_name)
    logger.info('File downloaded from S3 bucket successfully.')

    with open(object_name) as json_file:
        data = json.load(json_file)
        print(data['employees'])
        for emp in data['employees']:
            emp['name']='A'
        print(data['employees'])
    with open("modified.json", "w") as jsonfile:
        myJSON = json.dump(data, jsonfile) # Writing to the file
        upload_file('modified.json', bucket)
        jsonfile.close()

if __name__ == '__main__':
    main()
