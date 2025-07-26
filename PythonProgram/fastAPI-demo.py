from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class HelloRequest(BaseModel):
    name: str = "Guest"


@app.get("/")
def get_hello():
    return {"message": "Welcome To FastAPI!"}

@app.get("/api/hello")
def get_hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/api/hello")
def post_hello(request: HelloRequest):
    return {"message": f"Hello {request.name}!"}

