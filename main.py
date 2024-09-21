from fastapi import FastAPI , Response , status , HTTPException , Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange 
import psycopg2
from psycopg2.extras import DictCursor
import time
from sqlalchemy.orm import Session
from .Models import models   
from .database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)



app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db    
    finally:
        db.close()


class post(BaseModel):
    title: str
    content: str
    published : bool = True 

while True:


    try:
        conn =psycopg2.connect(host='localhost', database='Fastapi', user='postgres', password='9637311178', cursor_factory=DictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error: 
        print("coneecting to data base failed")
        print("Error: ", error)
        time.sleep(2)


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title":"favorite food", "content": "I like pizza", "id": 2}]



@app.get("/")
def home():
    return {"Welcome to my fast API function"}

@app.get("/")
def test_posts(db: Session = Depends(get_db)):
    return {"status":"success"}


@app.get("/posts")
def get_posts():
    posts = cursor.execute("""SELECT * FROM posts """)
    print(posts)
    return {"Data": "my_posts"}


@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}



@app.post("/myposts")
def create_posts(new_post:post):
    print(new_post.title)
    return {"Data": "new post"}


