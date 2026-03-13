from app.repositories.s3_repository import upload_file_to_s3


async def upload_dataset(file):
    bucket_name = "ai-data-lake-bucket"
    key = file.filename  # bucket S3

    upload_file_to_s3(file.file, bucket_name, key)
    return {
        "message": f"Arquivo '{file.filename}' enviado com sucesso para o bucket '{bucket_name}'",
        "filename": key,
    }
