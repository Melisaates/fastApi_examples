'''from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
#async def read_items(q: Union[str, None] = Query(default=..., max_length=50)): #3 nokta bir q değerinin olduğunu fakat none diye de bir değer olduğunu söyler.
async def read_items(q: Union[str, None] = Query(default=None, title="Query string",max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''