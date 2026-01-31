from fastapi import APIRouter
from services.analysis_service import analyze_idea

router = APIRouter()

@router.post('/analyze')
def analyze(idea: str):
    return analyze_idea(idea)
