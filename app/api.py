from fastapi import FastAPI
from app.router import datasets

app = FastAPI(title="AI Data Lake API", version="1.0")

app.include_router(datasets.router)  # Adicione suas rotas aqui

@app.get("/")
def read_root():
    return {"Teste": "Eita poxaaaa"}