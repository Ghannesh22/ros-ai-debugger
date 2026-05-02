from fastapi import FastAPI

from app.api.routes import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="ROS AI Debugger API",
        description="Backend API for text-based ROS and ROS 2 debugging assistance.",
        version="0.1.0",
    )
    app.include_router(api_router)
    return app


app = create_app()
