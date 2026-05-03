from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router

LOCAL_FRONTEND_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]


def create_app() -> FastAPI:
    app = FastAPI(
        title="ROS AI Debugger API",
        description="Backend API for text-based ROS and ROS 2 debugging assistance.",
        version="0.1.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=LOCAL_FRONTEND_ORIGINS,
        allow_credentials=False,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )
    app.include_router(api_router)
    return app


app = create_app()
