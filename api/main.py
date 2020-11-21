from fastapi import FastAPI

from .search import Search
from .fetch import Fetch

app = FastAPI()


@app.get("/")
async def index():
    return "Hello, World!"


@app.get("/search/q/{query}")
async def search(query: str):
    q = Search()
    return await q.get(query)


@app.get("/id/{drama_id}")
async def fetch(drama_id: str):
    f = Fetch()
    return await f.get(drama_id)
