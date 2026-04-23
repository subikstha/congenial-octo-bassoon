from sqlite3 import IntegrityError
from model.creature import Creature
from errors import Missing, Duplicate
from data.init import conn, curs

curs.execute(""" 
    create table if not exists creature(
        name text primary key,
        description text,
        country text,
        area text,
        aka text
    )
""")

# This init() function makes the connection to the sqlite3 and the database fake cryptid.db, 
# def init():
#     curs.execute("create table creature(name, description, country, area, aka)")

# row_to_model converts a tuple returned by a fetch function to a model object
def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name=name, description=description, country=country, area=area, aka=aka)

# model_to_dict() translates a Pydantic model to a dictionary, sutable for use as a named query parameter
def model_to_dict(creature: Creature) -> dict:
    return creature.dict()

def get_one(name: str) -> Creature:
    qry = """Select * from creature where name=:name"""
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Creature {name} not found")

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(creature: Creature):
    if not creature: return None
    qry = """insert into creature (name, description, country, area, aka) values (:name, :description,:country, :area, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"Creature {creature.name} already exists")
    conn.commit()
    return get_one(creature.name)

def modify(name: str,creature: Creature) -> Creature:
    if not (name and creature): return None
    qry = """ 
        update creature
        set name=:name,
        country=:country,
        area=:area,
        description=:description,
        aka=:aka
        where name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(f"Creature {creature.name} not found")

def replace(creature: Creature):
    return creature

def delete(name: str):
    qry = "delete from creature where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return True
    else:
        raise Missing(f"Creature {name} not found")
