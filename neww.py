#from enum import Enum
from typing import Union,List,Set
from fastapi import FastAPI, Query, Body, Form
from pydantic import BaseModel
from pydantic import Required



"""
@app.get("/items/{item_id}")
async def root(item_id: int):
    return {"hello world",item_id}"""


"""@app.get("/users/me")
async def read_user_me():
    return{"user_id":"current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id":user_id}"""

"""class Color(str,Enum):
    blue:"blue"
    purple:"purple"
    yellow:"yellow"



@app.get("/colors/{color_name}")
async def get_color(color_name:Color):
    if color_name==Color.blue:
        return {"color_name":color_name,"message":"offffff"}
    if color_name.value=="purple":
        return{"color_name":color_name,"message":"olleyyyy"}
    return{"color_name":color_name}

"""

"""@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return{"file_path":file_path}
"""

"""app=FastAPI()
@app.get("/items/{item_id}/users/{user_id}")
async def read_item(item_id:str,user_id:int, needy:str,q:Union[str,None]=Query(max_length=50,default=None,regex="^fixedquery$"),short:bool=False, skip: int=0, limit: Union[int, None] = None):
    item={"item_id": item_id, "owner_id": user_id,"needy":needy, "skip": skip, "limit": limit}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
"""

"""class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
app=FastAPI()

@app.post("/items/{item_id}")
async def create_item(item_id:int,item:Item):
    return {"item_id":item_id,**item.dict()}
"""


"""
app =FastAPI()
@app.get("/items/")
async def read_item(q:Union[str,None]=Query(default=Required,min_length=1)):
    result={"item_id":"melisa"}
    if q:
        result.update({"q":q})
    return result"""


"""app =FastAPI()
@app.get("/items/")
async def read_item(q:list=Query(default=[])):
    result={"item_id":"melisa"}
    if q:
        result.update({"q":q})
    return result"""
"""
app =FastAPI()
@app.get("/items/")
async def read_item(q:Union[str,None]=Query(default=None),importance:int=Body()):
    result={"item_id":"melisa","importance":importance}
    if q:
        result.update({"q":q})
    
    return result

"""
"""class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
app=FastAPI()
@app.put("/item/{item_id}")
async def update_item(item:Union[Item,None]=Body(embed=True),item_id=int):
    return{"item_id":item_id,"item":item}

"""

"""
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags:Set[str]=set() #List[str]=[]
app=FastAPI()
@app.put("/item/{item_id}")
async def update_item(item:Item,item_id=int):
    return{"item_id":item_id,"item":item}

"""

"""from typing import Set, Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[List[Image], None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
"""


"""from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights"""

"""app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results"""

"""app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results"""

"""from typing import Union

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}"""

"""from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}"""
"""
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user"""

"""from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)#exclude fazladan olanları yazmaz.
async def read_item(item_id: str):
    return items[item_id]"""


    #userıdli ör yap

app=FastAPI()

@app.post("/login/")
async def create_item(username:str=Form(),password:int=Form()):
    return {"username":username}