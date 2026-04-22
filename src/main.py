try:
    from .web.explorer import router
except ImportError:
    from web.explorer import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

@app.get('/')
def top():
    return 'top here'

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)