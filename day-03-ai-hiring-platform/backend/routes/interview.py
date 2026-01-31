from fastapi import APIRouter
from services.ai_question_service import generate_questions
from services.ai_scoring_service import score_answer

router = APIRouter(prefix='/interview')

@router.post('/generate')
def generate(role: str):
    return {'questions': generate_questions(role)}

@router.post('/score')
def score(answer: str):
    return score_answer(answer)
