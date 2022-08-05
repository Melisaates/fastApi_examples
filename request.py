from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q:Union[str,None]=None):
    result= {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q":q})
    return result





'''async def create_item(item:Item):
    item_dict=item_dict()
    if item.tax:
        price_with_tax= item.tax+item.price
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict    
    return item'''

