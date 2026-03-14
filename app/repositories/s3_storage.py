import boto3
from app.repositories.storage_interface import StorageInterface

class S3Storage(StorageInterface):
    
    def __init__(self):
        self.s3 = boto3.client("s3")

    def upload_dataset(self, file, filename: str):
        bucket = "ai-data-lake-bucket"
        self.s3.upload_fileobj(file, bucket, filename)
        
        return filename