from fastapi import FastAPI
from routes.expense import router as expense_router

app = FastAPI(title='AI Finance Insight API')
app.include_router(expense_router, prefix='/expense')
