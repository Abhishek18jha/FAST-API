from fastapi import APIRouter
from app.models.loan_models import LoanRequest, LoanResponse
from app.services.processing import calculate_amortization

# Create an APIRouter instance
# prefix: Adds a base path to all routes in this file (e.g., /calculate/loan/)
# tags: Used by FastAPI to group routes in the /docs UI (e.g., "Loan Calculations")
router = APIRouter(
    prefix="/calculate",
    tags=["Financial Operations"],
)

@router.post("/loan/", response_model=LoanResponse)
def loan_calculator(request: LoanRequest):
    """
    Calculates monthly payment and total interest based on structured input.
    """
    response = calculate_amortization(request)
    return response