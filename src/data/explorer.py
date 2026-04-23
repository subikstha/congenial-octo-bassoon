from .init import curs, conn
from model.explorer import Explorer

curs.execute(""" 
    create table if not exists explorer(
        name text primary key,
        description text,
        country text
    )
""")

# This init() function makes the connection to the sqlite3 and the database fake cryptid.db, 
# def init():
#     curs.execute("create table creature(name, description, country, area, aka)")

# row_to_model converts a tuple returned by a fetch function to a model object
def row_to_model(row: tuple) -> Explorer:
    name, description, country = row
    return Explorer(name=name, description=description, country=country)

# model_to_dict() translates a Pydantic model to a dictionary, sutable for use as a named query parameter
def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None

def get_one(name: str) -> Explorer:
    qry = """Select * from explorer where name=:name"""
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer):
    qry = """insert into explorer values (:name, :description, :country)"""
    params = model_to_dict(explorer)
    curs.execute(qry, params)
    conn.commit()
    return get_one(explorer.name)

def modify(explorer: Explorer):
    qry = """ 
        update explorer set country = :country,
        name=:name,
        description=:description,
        where name=:name_orig
    """
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    _ = curs.execute(qry, params)
    return get_one(explorer.name)

def replace(explorer: Explorer):
    return explorer

def delete(explorer: Explorer):
    qry = "delete from creature where name = :name"
    params = {"name": explorer.name}
    curs.execute(qry, params)
