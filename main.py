from typing import Union
from enum import Enum
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status


app = FastAPI()


class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


@app.get("/")
async def read_root():
    return {"Message": "Hello World"}


@app.get("/role/{role}")
async def role(role: Role):
    if role is Role.ADMIN:
        return JSONResponse(
            content={"role": role, "message": "You are an admin"},
            status_code=status.HTTP_200_OK,
        ) 
    elif role is Role.USER:
        return JSONResponse(
            content={"role": role, "message": "You are a user"},
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content={"role": None, "message": "Invalid Role"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@app.get("/user/{name}")
async def user(name: str):
    print(name)
    return JSONResponse(
        content={
            "id": 1,
            "name": name,
            "age": 27,
        },
        status_code=status.HTTP_200_OK,
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
