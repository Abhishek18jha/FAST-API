from pydantic import BaseModel
from ..models.data_models import BaseModel
# --- ENDPOINT 2: TEXT ANALYSIS MODELS ---

class TextAnalysisRequest(BaseModel):
    """Input model for text processing."""
    text_input: str
    word_to_find: str
    
class TextAnalysisResponse(BaseModel):
    """Output model for text analysis results."""
    original_length: int
    found_count: int
    unique_words: int
    is_present: bool
    summary: str