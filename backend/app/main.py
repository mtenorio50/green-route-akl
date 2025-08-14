from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import transit

app = FastAPI(title="GreenRoute AKL API", version="0.1.0")

# Allow local dev for React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transit.router)
