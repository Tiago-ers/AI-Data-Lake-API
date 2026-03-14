from fastapi import HTTPException
from app.repositories.s3_storage import S3Storage
from app.repositories.local_storage import LocalStorage

# Função para upload de dataset, escolhendo entre S3 ou armazenamento local
async def upload_dataset(file, storage_type: str = "local"):
    try:
        
        if storage_type == "s3":
            storage = S3Storage()
        elif storage_type == "local":
            storage = LocalStorage()
        else:
            raise ValueError("Tipo de armazenamento inválido. Use 'local' ou 's3'.")
       
        result = storage.upload_dataset(file.file, file.filename)
        
        return {
            "message": f"Arquivo '{file.filename}' enviado com sucesso para o {storage_type}",
            "location": result,
        }
    except Exception as e:
        raise HTTPException(
           status_code=500,
            detail=f"Erro ao enviar o arquivo '{file.filename}' para : {str(e)}"
        )    
