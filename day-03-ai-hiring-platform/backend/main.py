from fastapi import FastAPI
from routes import auth, recruiter, candidate, interview

app = FastAPI(title='AI Hiring Platform')

app.include_router(auth.router)
app.include_router(recruiter.router)
app.include_router(candidate.router)
app.include_router(interview.router)
