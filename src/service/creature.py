import os
USE_SQLITE = os.getenv("USE_SQLITE", "false")
from model.creature import Creature
if USE_SQLITE:
    import data.creature as data
else:
    import fake.creature as data

def get_all():
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(name)

def create(creature: Creature) -> Creature:
    return data.create(creature)
def replace(id, creature: Creature) -> Creature:
    return data.replace(id, creature)
def modify(id, creature: Creature) -> Creature:
    return data.modify(id, creature)
def delete(id, creature: Creature) -> bool:
    return data.delete(id)