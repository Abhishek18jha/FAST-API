from fastapi import FastAPI
# Import the router objects from the new files
from app.routers import loan_router, text_router 

# The main application instance
app = FastAPI(title="Data Operations Hub API")

# --- INCLUDE THE SEGREGATED ROUTERS ---

# 1. Include the Loan Router
app.include_router(loan_router.router)

# 2. Include the Text Router
app.include_router(text_router.router)

# --- Root Endpoint (Remains in main.py) ---
@app.get("/")
def read_root():
    """
    Root endpoint to confirm API is running.
    """
    return {"message": "API is running. Visit /docs for documentation."}

# You can add global error handling, middleware, etc., here in main.py
# without cluttering the individual route definitions.