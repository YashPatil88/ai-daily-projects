from fastapi import APIRouter

router = APIRouter(prefix='/candidate')

@router.get('/interviews')
def interviews():
    return {'message': 'Candidate interview list'}
