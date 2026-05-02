from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.models import AnalysisResponse, AnalyzeTextRequest
from app.services import UploadedFileContext, analyze_ros_input

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


@router.post("/text", response_model=AnalysisResponse)
def analyze_text(request: AnalyzeTextRequest) -> AnalysisResponse:
    return analyze_ros_input(
        text=request.text,
        filename=request.filename,
        ros_version_hint=request.ros_version_hint,
    )


@router.post("/files", response_model=AnalysisResponse)
async def analyze_files(
    files: Annotated[list[UploadFile] | None, File()] = None,
    ros_version_hint: Annotated[str | None, Form()] = None,
) -> AnalysisResponse:
    if not files:
        raise HTTPException(
            status_code=400,
            detail="At least one file must be uploaded.",
        )

    uploaded_file_context: list[UploadedFileContext] = []

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

        content = (await uploaded_file.read()).decode("utf-8", errors="replace")
        uploaded_file_context.append(
            UploadedFileContext(filename=filename, content=content)
        )

    return analyze_ros_input(
        ros_version_hint=ros_version_hint,
        uploaded_files=uploaded_file_context,
    )
