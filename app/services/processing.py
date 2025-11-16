import uuid
from math import pow
from ..models.data_models import BaseModel

from ..models.loan_models import LoanRequest, LoanResponse
from ..models.text_models import TextAnalysisRequest, TextAnalysisResponse

# --- LOGIC FOR LOAN CALCULATION ---
def calculate_amortization(req: LoanRequest) -> LoanResponse:
    """Calculates monthly payment and total interest."""
    
    principal = req.principal
    annual_rate = req.rate_percent
    years = req.years

    monthly_rate = annual_rate / 12 / 100
    n_payments = years * 12
    loan_id = str(uuid.uuid4())

    # Amortization Formula: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1 ]
    if monthly_rate > 0:
        monthly_payment = principal * (monthly_rate * pow(1 + monthly_rate, n_payments)) / (pow(1 + monthly_rate, n_payments) - 1)
    else:
        # Simple case for 0% interest
        monthly_payment = principal / n_payments
    
    total_payment = monthly_payment * n_payments
    total_interest = total_payment - principal

    # Create and return the structured response model
    return LoanResponse(
        loan_id=loan_id,
        monthly_payment=round(monthly_payment, 2),
        total_interest=round(total_interest, 2),
        total_payment=round(total_payment, 2),
        status="PROCESSED"
    )

# --- LOGIC FOR TEXT ANALYSIS ---
def analyze_text(req: TextAnalysisRequest) -> TextAnalysisResponse:
    """Performs simple text statistics and word counting."""
    
    text = req.text_input
    target = req.word_to_find
    
    # 1. Word Count
    words = text.lower().split()
    
    # 2. Unique Words
    unique_words_set = set(words)
    
    # 3. Target Word Count
    found_count = words.count(target.lower())
    
    # 4. Summary
    summary = f"Analyzed {len(words)} words. Target word '{target}' found {found_count} times."

    # Create and return the structured response model
    return TextAnalysisResponse(
        original_length=len(text),
        found_count=found_count,
        unique_words=len(unique_words_set),
        is_present=(found_count > 0),
        summary=summary
    )