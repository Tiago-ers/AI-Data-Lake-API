from fastapi import APIRouter, UploadFile, File
from app.services.dataset_service import upload_dataset

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    result = await upload_dataset(file)
    return {"message": result}