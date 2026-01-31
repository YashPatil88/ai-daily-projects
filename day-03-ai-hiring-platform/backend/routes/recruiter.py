from fastapi import APIRouter

router = APIRouter(prefix='/recruiter')

@router.get('/dashboard')
def dashboard():
    return {'message': 'Recruiter dashboard data'}
