from fastapi import APIRouter
from app.models.text_models import TextAnalysisRequest, TextAnalysisResponse
from app.services.processing import analyze_text

# Create a separate APIRouter instance
router = APIRouter(
    prefix="/analyze",
    tags=["Text Analysis"],
)

@router.post("/text/", response_model=TextAnalysisResponse)
def text_analyzer(request: TextAnalysisRequest):
    """
    Performs word count and basic text statistics.
    """
    response = analyze_text(request)
    return response