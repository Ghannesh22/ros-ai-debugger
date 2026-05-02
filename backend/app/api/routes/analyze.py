from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.models import AnalysisResponse, AnalyzeTextRequest

router = APIRouter(prefix="/analyze", tags=["analysis"])

SUPPORTED_FILE_EXTENSIONS = {
    ".cpp",
    ".launch",
    ".log",
    ".py",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
SUPPORTED_EXACT_FILENAMES = {"cmakelists.txt", "package.xml"}
SUPPORTED_FILE_TYPES_MESSAGE = (
    ".txt, .log, .launch, .xml, .yaml, .yml, .py, .cpp, "
    "CMakeLists.txt, package.xml"
)


def _is_supported_filename(filename: str) -> bool:
    normalized_filename = filename.lower()
    if normalized_filename in SUPPORTED_EXACT_FILENAMES:
        return True

    return any(
        normalized_filename.endswith(extension)
        for extension in SUPPORTED_FILE_EXTENSIONS
    )


def _placeholder_response(
    *,
    summary: str,
    related_files: list[str],
    ros_version_guess: str = "unknown",
) -> AnalysisResponse:
    return AnalysisResponse(
        summary=summary,
        detected_errors=[],
        likely_root_causes=[],
        recommended_fixes=[],
        verification_commands=[],
        confidence="low",
        ros_version_guess=ros_version_guess,
        related_files=related_files,
        next_debugging_steps=[],
    )


@router.post("/text", response_model=AnalysisResponse)
def analyze_text(request: AnalyzeTextRequest) -> AnalysisResponse:
    related_files = [request.filename] if request.filename else []

    return _placeholder_response(
        summary="Text received for analysis. Analyzer logic will be added in Phase 2.5.",
        ros_version_guess=request.ros_version_hint or "unknown",
        related_files=related_files,
    )


@router.post("/files", response_model=AnalysisResponse)
async def analyze_files(
    files: Annotated[list[UploadFile] | None, File()] = None,
) -> AnalysisResponse:
    if not files:
        raise HTTPException(
            status_code=400,
            detail="At least one file must be uploaded.",
        )

    related_files: list[str] = []

    for uploaded_file in files:
        filename = uploaded_file.filename or ""
        if not filename or not _is_supported_filename(filename):
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Unsupported file type: {filename or 'unnamed file'}. "
                    f"Supported files: {SUPPORTED_FILE_TYPES_MESSAGE}."
                ),
            )

        await uploaded_file.read()
        related_files.append(filename)

    return _placeholder_response(
        summary="Files received for analysis. Analyzer logic will be added in Phase 2.5.",
        related_files=related_files,
    )
