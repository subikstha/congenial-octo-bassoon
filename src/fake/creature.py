from model.explorer import Creature

# fake data, replaced later by real DB and SQL
_creatures = [
    Creature(name = 'Emperor Penguin', country = 'Antarctica', area = 'Antarctica', description = 'The largest penguin', aka = 'Emperor'),
    Creature(name = 'Adelie Penguin', country = 'Antarctica', area = 'Antarctica', description = 'The smallest penguin', aka = 'Adelie'),
    Creature(name = 'Gentoo Penguin', country = 'Antarctica', area = 'Antarctica', description = 'The fastest penguin', aka = 'Gentoo'),
    Creature(name = 'Chinstrap Penguin', country = 'Antarctica', area = 'Antarctica', description = 'The most social penguin', aka = 'Chinstrap'),
    Creature(name = 'Macaroni Penguin', country = 'Antarctica', area = 'Antarctica', description = 'The most colorful penguin', aka = 'Macaroni'),
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    return creature

def modify(creature: Creature) -> Creature:
    return creature

def replace(name: str, creature: Creature) -> Creature:
    return creature

def delete(name: str) -> bool:
    return None