
import os
import boto3
from botocore.exceptions import NoCredentialsError


class S3Sync:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def sync_folder_to_s3(self, folder, aws_bucket_url):
        """
        Sync local folder to S3 bucket.
        aws_bucket_url should be in format s3://bucket-name/path/
        """
        try:
            bucket_name = aws_bucket_url.split('/')[2]
            s3_prefix = '/'.join(aws_bucket_url.split('/')[3:]).strip('/')
            if s3_prefix and not s3_prefix.endswith('/'):
                s3_prefix += '/'

            for root, dirs, files in os.walk(folder):
                for file in files:
                    local_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_path, folder)
                    s3_key = os.path.join(s3_prefix, relative_path).replace('\\', '/')
                    self.s3_client.upload_file(local_path, bucket_name, s3_key)
        except NoCredentialsError:
            print("Credentials not available")
        except Exception as e:
            print(f"Error syncing to S3: {e}")

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        """
        Sync from S3 bucket to local folder.
        aws_bucket_url should be in format s3://bucket-name/path/
        """
        try:
            bucket_name = aws_bucket_url.split('/')[2]
            s3_prefix = '/'.join(aws_bucket_url.split('/')[3:]).strip('/')
            if s3_prefix and not s3_prefix.endswith('/'):
                s3_prefix += '/'

            paginator = self.s3_client.get_paginator('list_objects_v2')
            for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
                for obj in page.get('Contents', []):
                    s3_key = obj['Key']
                    relative_path = os.path.relpath(s3_key, s3_prefix)
                    local_path = os.path.join(folder, relative_path)
                    os.makedirs(os.path.dirname(local_path), exist_ok=True)
                    self.s3_client.download_file(bucket_name, s3_key, local_path)
        except NoCredentialsError:
            print("Credentials not available")
        except Exception as e:
            print(f"Error syncing from S3: {e}")
