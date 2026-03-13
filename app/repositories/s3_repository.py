import boto3

s3 = boto3.client("s3")

def upload_file_to_s3(file, bucket_name, key):
    s3.upload_fileobj(file, bucket_name, key)