from fastapi import APIRouter
from app.services.NOME_MODULO import create, getOne, getAll, update, delete

router = APIRouter()

@router.post()
async def create(payload):
    return create(payload)

@router.get("/{id}")
async def getOne(id):
    return getOne(id)

@router.get("/")
async def getAll():
    return getAll()

@router.put("/{id}")
async def update(id, payload):
    return update(id, payload)

@router.delete("/{id}")
async def delete(id):
    return delete(id)
