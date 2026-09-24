from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def read_posts():
    return [{
        'username' : 'Rick'
    }]