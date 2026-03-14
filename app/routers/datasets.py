from fastapi import APIRouter, UploadFile, File
from app.services.dataset_service import upload_dataset

router = APIRouter(prefix="/datasets", tags=["datasets"])

# Endpoint para upload de datasets com opção de armazenamento local ou S3
@router.post("/upload")
async def upload(file: UploadFile = File(...), storage: str = "local"):   
    return await upload_dataset(file, storage)