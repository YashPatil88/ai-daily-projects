from fastapi import FastAPI
from routes.idea import router as idea_router

app = FastAPI(title='AI Startup Idea Validator')
app.include_router(idea_router, prefix='/idea')
