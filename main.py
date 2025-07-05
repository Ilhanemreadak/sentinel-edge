# main.py
from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI(
    title="Sentinel Edge API",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
)

app.include_router(api_router, prefix="/api")
