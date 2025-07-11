from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/{user_id}")
def read_user(user_id: str):
    print("prueba de read_user" + user_id)
    return(user_id)