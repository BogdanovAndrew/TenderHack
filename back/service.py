from fastapi import APIRouter

import back.schemas as schemas
from core.validator import correct_req


router = APIRouter()

@router.get('/ste', response_model=schemas.STE)
def get_ste(user_req: str):
    valid_name = correct_req(user_req)
    ste = schemas.STE(
        fullname=valid_name,
        chars=[
            'size',
            'type'
        ]
    )

    return ste