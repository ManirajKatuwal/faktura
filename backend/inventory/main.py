from fastapi import FastAPI
from .routes.auth import router as auth_router

app = FastAPI(title="Inventory Service")
app.include_router(auth_router, prefix="/api/v1")