from typing import Literal

from pydantic import BaseModel, Field

ConfidenceLevel = Literal["low", "medium", "high"]


class AnalyzeTextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Pasted ROS error text.")
    filename: str | None = Field(
        default=None,
        description="Optional source filename for pasted text.",
    )
    ros_version_hint: str | None = Field(
        default=None,
        description="Optional user-provided ROS version hint, such as ROS 1 or ROS 2.",
    )


class AnalysisResponse(BaseModel):
    summary: str = Field(
        ...,
        description="Short beginner-friendly explanation of the most likely issue.",
    )
    detected_errors: list[str] = Field(
        ...,
        description="Detected ROS error categories.",
    )
    likely_root_causes: list[str] = Field(
        ...,
        description="Likely reasons the detected issue happened.",
    )
    recommended_fixes: list[str] = Field(
        ...,
        description="Practical actions the user can try.",
    )
    verification_commands: list[str] = Field(
        ...,
        description="Commands the user can run in their ROS environment to verify.",
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="high for exact matches, medium for partial matches, low for unknown input.",
    )
    ros_version_guess: str = Field(
        ...,
        description="Best guess of ROS version context, such as ROS 1, ROS 2, or unknown.",
    )
    related_files: list[str] = Field(
        ...,
        description="Input filenames related to the diagnosis.",
    )
    next_debugging_steps: list[str] = Field(
        ...,
        description="Suggested next checks if the first fix does not solve the issue.",
    )
