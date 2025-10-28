from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="api-gateway")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.get("/")
async def root():
    return {"message": "API Gateway is running"} 
app.get("/health")
async def health_check():
    return {"status": "healthy"}   