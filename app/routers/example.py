from fastapi import APIRouter
from app.services.example import get_example_message

router = APIRouter()

@router.get("/example")
async def get_example():
    # Call the service function
    return {"message": get_example_message()}
