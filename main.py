from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published:bool = True
    rating: Optional[int] = None

@app.get("/") # if we comment out the this decorator this root() block of  code will have nothing to do with the fast api
def root():
    
    return {"message": "Welcome to My API"}

@app.get("/") # if we comment out the this decorator this root() block of  code will have nothing to do with the fast api
def root1():
    
    return {"message": "Welcome to My API 1"}#if we have two operations with the same decorator then which ever placed on top will be displayed and rest will not be displayed 
@app.get("/posts")
def  get_post():
    return {"data":"this is your post"}

@app.get("/1") # if we comment out the this decorator this root() block of  code will have nothing to do with the fast api
def root():
    
    return {"message": "this my world **bitch**"}


@app.get("/info") # if we comment out the this decorator this root() block of  code will have nothing to do with the fast api
def root():
    
    return {"message": "unicorn main:app --reload will help us workround restarting the entire server to see the changes to the code "}

@app.post("/createposts")
def create_posts(new_post : Post):
    print(new_post.rating)
    return {"data":"new post "}

# title str, content str. we just want these data sent by user and we don't want anything else for now  we can other values like published , bool 
