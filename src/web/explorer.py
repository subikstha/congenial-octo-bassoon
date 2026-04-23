from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
import service.explorer as service
from errors import Missing, Duplicate

router = APIRouter(prefix = '/explorer')

@router.get('/')
def get_all():
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Explorer | None:
    try:
        return service.get_one(name)
    except Missing as exec:
        raise HTTPException(status_code=404, detail=exec.msg)


@router.post('/')
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exec:
        raise HTTPException(status_code=404, detail=exec.msg)

@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    return service.modify(explorer)

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)


@router.delete("/{name}")
def delete(name: str):
    try:
        service.delete(name)
        return None
    except Missing as exec:
        raise HTTPException(status_code=404, detail=exec.msg)