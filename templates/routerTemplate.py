from fastapi import APIRouter
from app.services.NOME_RECURSO import create, getOne, getAll, update, delete

router = APIRouter("/")

@router.post("/")
async def create_endpoint(payload):
    return create(payload)

@router.get("/{id}")
async def getOne_endpoint(id):
    return getOne(id)

@router.get("/")
async def getAll_endpoint():
    return getAll()

@router.put("/{id}")
async def update_endpoint(id, payload):
    return update(id, payload)

@router.delete("/{id}")
async def delete_endpoint(id):
    return delete(id)