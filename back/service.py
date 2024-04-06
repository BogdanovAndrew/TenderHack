from fastapi import APIRouter

import schemas


router = APIRouter()

@router.get('/ste', response_model=schemas.STE)
def get_ste(user_req: str):
    ste = schemas.STE(
        fullname="Test",
        chars=[
            'size',
            'type'
        ]
    )

    return ste