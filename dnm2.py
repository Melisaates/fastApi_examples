from typing import List, Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
#async def read_items(q: Union[List[str], None] = Query(default=None)):
async def read_items(q: List = Query(default=[])):

    query_items = {"q": q}
    return query_items