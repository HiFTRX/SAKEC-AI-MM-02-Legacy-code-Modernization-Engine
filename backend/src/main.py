from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.analyzer import router as analyzer_router

app = FastAPI(title="Legacy Code Modernization Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyzer_router)

@app.get("/")
def home():
    return {"message": "Backend running"}