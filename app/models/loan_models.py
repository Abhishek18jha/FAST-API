from pydantic import BaseModel
from ..models.data_models import BaseModel

class LoanRequest(BaseModel):
    """Input model for loan amortization calculation."""
    principal: float
    rate_percent: float
    years: int

class LoanResponse(BaseModel):
    """Output model for calculated loan data."""
    loan_id: str
    monthly_payment: float
    total_interest: float
    total_payment: float
    status: str
