from app.repositories.storage_interface import StorageInterface
from pathlib import Path
import shutil

DATASET_PATH = Path("storage/datasets")

class LocalStorage(StorageInterface):
    
    def upload_dataset(self, file, filename: str):
        
        DATASET_PATH.mkdir(parents=True, exist_ok=True)
        
        destination = DATASET_PATH / filename
        
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file, buffer)
            
        return str(destination)