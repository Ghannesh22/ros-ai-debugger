from fastapi import APIRouter

from app.models import AnalysisResponse, AnalyzeTextRequest

router = APIRouter(prefix="/analyze", tags=["analysis"])


@router.post("/text", response_model=AnalysisResponse)
def analyze_text(request: AnalyzeTextRequest) -> AnalysisResponse:
    related_files = [request.filename] if request.filename else []

    return AnalysisResponse(
        summary="Text received for analysis. Analyzer logic will be added in Phase 2.5.",
        detected_errors=[],
        likely_root_causes=[],
        recommended_fixes=[],
        verification_commands=[],
        confidence="low",
        ros_version_guess=request.ros_version_hint or "unknown",
        related_files=related_files,
        next_debugging_steps=[],
    )
