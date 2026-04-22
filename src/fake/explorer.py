from model.explorer import Explorer

# fake data, replaced later by real DB and SQL
_explorers = [
    Explorer(name = 'Richard Byrd', country = 'USA', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Roald Amundsen', country = 'Norway', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Robert Falcon Scott', country = 'UK', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Ernest Shackleton', country = 'UK', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Sir Edmund Hillary', country = 'New Zealand', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Sir Vivian Fuchs', country = 'UK', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Sir Douglas Mawson', country = 'Australia', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Sir Ernest Shackleton', country = 'UK', description = 'Explorer of the Antarctic'),
    Explorer(name = 'Sir Douglas Mawson', country = 'Australia', description = 'Explorer of the Antarctic'),
]

def get_all() -> list[Explorer]:
    # Returns all explorers
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(explorer: Explorer) -> Explorer:
    return explorer

def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer

def delete(name: str) -> bool:
    return None