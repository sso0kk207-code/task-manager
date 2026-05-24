from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import auth

app = FastAPI(
    title="FastAPI Task-manager",
    description="Приложение для тайм-менджмента",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "FastAPI Task-manager app. Go to /docs for API documentation"}

@app.get("/health-check")
async def health_check():
    return {"status": "ok"}