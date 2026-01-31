from fastapi import APIRouter
from services.analysis_service import analyze_expenses

router = APIRouter()

@router.post('/analyze')
def analyze(data: dict):
    return analyze_expenses(data.get('expenses', []))
