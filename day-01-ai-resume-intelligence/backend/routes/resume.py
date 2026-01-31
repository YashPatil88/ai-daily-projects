from fastapi import APIRouter, UploadFile
from services.resume_analyzer import analyze_resume

router = APIRouter()

@router.post('/analyze')
async def analyze(file: UploadFile):
    content = await file.read()
    return analyze_resume(content.decode())
