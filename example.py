from enum import Enum
from turtle import st
from unittest import skip
from fastapi import FastAPI
from typing import Union

app = FastAPI()

'''
@app.get("/items/{item_id}")
async def read_item(item_id:str,needy:str,skip:int=0,limit:Union[str,None]=None):
    item={"item_id":item_id,"needy":needy,"skip":skip,"limit":limit}
    return item'''

'''@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}    

''''''
@app.get("/files/{file_path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
'''


@app.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id: str, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "user_id": user_id}

    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"tanım": "kardeşler"}
        )

    return item