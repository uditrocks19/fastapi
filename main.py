from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
async def read_root():
    return {"Message" : "Hello World"}

# @app.get('/greet/{name}')
# async def greet_name(name:str) ->dict:
#     return {"Message": f"Hello {name}, How you doing!"}

# @app.get('/greet')
# async def greet_name_with_query_parameter(name:str) ->dict:
#     return {"Message": f"Hello {name}, How you doing!"}

@app.get('/greet/{name}')
async def greet_name_with_query_parameter(name:str, age:int) ->dict:
    return {"Message": f"Hello {name}, age : {age}, How you doing!"}


@app.get('/greet')
async def greet_name_with_query_parameter(name:Optional[str] = "User", age:int = 0) ->dict:
    return {"Message": f"Hello {name}, How you doing!",
            "age": age
        }

class BookCreateModel(BaseModel):
    title : str
    Author : str


@app.post('/create_book')
async def create_book(book_data : BookCreateModel):
    return {
        "title" : book_data.title,
        "Author" : book_data.Author
    }


@app.get('/get_headers', status_code=200)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers['Accept'] = accept
    request_headers['Content-Type'] = content_type
    request_headers['User-Agent'] = user_agent
    request_headers['Host'] = host
    return request_headers

