from fastapi import APIRouter, HTTPException
from model.creature import Creature
import service.creature as service
from errors import Missing, Duplicate

router = APIRouter(prefix = '/creature')

@router.get('/')
def get_all():
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Creature | None:
    try:
        return service.get_one(name)
    except Missing as exec:
        raise HTTPException(status_code=404, detail=exec.msg)
    
@router.post('/')
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exec:
        raise HTTPException(status_code=400, detail=exec.msg)

@router.patch("/")
def modify(name: str, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as exec:
        raise HTTPException(status_code=404, detail=exec.msg)

@router.put("/")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)


@router.delete("/{name}", status_code=204)
def delete(name: str) -> None:
    try:
        service.delete(name)
        return None
    except Missing as exec:
        raise HTTPException(status_code=404, detail=exec.msg)