from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published : bool = True 



@app.get("/multiply")
def calculate_sum(a: int, b: int):
    result = a * b
    return {"multiply": result}


@app.get("/")
def home():
    return {"Welcome to my fast API function"}


@app.get("/Add")
def calculate_sum(a: int, b: int):
    result = a + b
    return {"Sum": result}


@app.get("/Abid")
def calculate_sum():
    return {"Abid is amazing guy"}



@app.get("/posts")
def get_posts():
    return {"Data": "this is my post"}


@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}



@app.post("/myposts")
def create_posts(new_post:post):
    print(new_post.title)
    return {"Data": "new post"}
