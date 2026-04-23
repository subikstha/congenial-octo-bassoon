from .init import curs, conn
from model.creature import Creature

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
    return row_to_model(row)

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(creature: Creature):
    qry = """insert into creature values (:name, :description,:country, :area, :aka)"""
    params = model_to_dict(creature)
    curs.execute(qry, params)
    conn.commit()
    return get_one(creature.name)

def modify(creature: Creature):
    qry = """ 
        update creature set country = :country,
        name=:name,
        description=:description,
        area=:area,
        aka=:aka
        where name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(qry, params)
    return get_one(creature.name)

def replace(creature: Creature):
    return creature

def delete(creature: Creature):
    qry = "delete from creature where name = :name"
    params = {"name": creature.name}
    curs.execute(qry, params)
