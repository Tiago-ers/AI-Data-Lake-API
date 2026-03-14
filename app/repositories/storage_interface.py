from abc import ABC, abstractmethod

class StorageInterface(ABC):
    
    @abstractmethod
    async def upload_dataset(self, file, filename: str):
        pass