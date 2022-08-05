'''from fastapi import FastAPI,Form,File,UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file:bytes=File(),fileb:UploadFile=File(),token:str=Form()):
    return {#"filename":file.filename,
            "file_size":len(file),
            "token":token,
            "fileb_content_type":fileb.content_type
            }'''

from typing import Set, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["items"])
async def read_users():
    return [{"username": "johndoe"}]
