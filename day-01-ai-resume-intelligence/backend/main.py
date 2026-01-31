from fastapi import FastAPI
from routes.resume import router as resume_router

app = FastAPI(title='AI Resume Intelligence API')

app.include_router(resume_router, prefix='/resume')
