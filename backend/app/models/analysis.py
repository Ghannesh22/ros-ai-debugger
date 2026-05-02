from pydantic import BaseModel, Field


class AnalyzeTextRequest(BaseModel):
    text: str = Field(..., min_length=1)
    filename: str | None = None
    ros_version_hint: str | None = None


class AnalysisResponse(BaseModel):
    summary: str
    detected_errors: list[str]
    likely_root_causes: list[str]
    recommended_fixes: list[str]
    verification_commands: list[str]
    confidence: str
    ros_version_guess: str
    related_files: list[str]
    next_debugging_steps: list[str]
