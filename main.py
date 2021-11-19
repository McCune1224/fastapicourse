import random
from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "t1", "content": "content 1", "id": 1},{"title": "t2", "content": "content 2", "id": 2} ]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Post ID: {id}"} 

@app.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
#title str, content str
