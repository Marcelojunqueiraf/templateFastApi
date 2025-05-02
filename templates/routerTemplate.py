from fastapi import APIRouter
from app.services.NOME_RECURSO import create, getOne, getAll, update, delete

router = APIRouter()

@router.post("", status_code=201)
async def create_endpoint(payload):
    return create(payload)

@router.get("/{id}", status_code=200)
async def getOne_endpoint(id):
    return getOne(id)

@router.get("/", status_code=200)
async def getAll_endpoint():
    return getAll()

@router.put("/{id}", status_code=200)
async def update_endpoint(id, payload):
    return update(id, payload)

@router.delete("/{id}", status_code=204)
async def delete_endpoint(id):
    return delete(id)