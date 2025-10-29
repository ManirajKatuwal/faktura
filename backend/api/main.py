from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#service URLs
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")
INVENTORY_SERVICE_URL = os.getenv("INVENTORY_SERVICE_URL", "http://inventory-service:8002")

#proxy function
async def proxy_request(service_url: str, path: str, request: Request):
    async with httpx.AsyncClient() as client:
        try:
            method = request.method
            body = await request.body()
            headers = dict(request.headers)
            url = f"{service_url}/{path}"
            response = await client.request(method, url, content=body, headers=headers)
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def auth_proxy(path: str, request: Request):
    return await proxy_request(AUTH_SERVICE_URL, path, request)

@app.api_route("/inventory/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def inventory_proxy(path: str, request: Request):
    return await proxy_request(INVENTORY_SERVICE_URL, path, request)

@app.get("/")
async def root():
    return {"message": "API Gateway is running"}
