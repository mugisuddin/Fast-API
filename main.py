from fastapi import FastAPI , Response , status , HTTPException , Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import time
from sqlalchemy.orm import session
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, sessionLocal 

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='Fastapi', user='postgres', password='9637311178', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection wass succesfull")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title":"favorite food", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i 
        
@app.get("/sqlalchemy")
def test_posts(db: session = Depends(get_db)):
    return {"status": "success"}


@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)    
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"details": post}

@app.get("/posts/{id}")
def get_posts(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_details": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
       
    

    my_posts.pop(index)

    return { "message": 'post successfully deleted'}

@app.put("/posts/{id}")
def update_post(id: int, post: post):

    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] - post_dict
    return {"data": post_dict}









 


