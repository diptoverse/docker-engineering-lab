from fastapi import APIRouter, Depends

from app.schemas.user import UserCreate
from app.services.user_service import create_user
from app.dependencies import get_app_version


router = APIRouter()

@router.get("/users")
def get_users():
    return{
        "users":[
            "Dipto",
            "Murati"
        ]
    }

@router.post("/users")
def create_user_endpoint(user: UserCreate):
    return create_user(user)

@router.get("/version")
def get_version(
    version = Depends(get_app_version)
):
    return{
        "application_version": version
    }