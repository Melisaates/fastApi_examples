from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(item_id:int=Path(title="The ID of the item to get",ge=0,le=100),
q:Union[str,None]=Query(default=None,alias="item_query"),
size:float=Query(gt=0,lt=10.5)):
    result={"item_id":item_id,"size":size}
    if q:
        result.update({"q":q})
    return result




'''
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results'''