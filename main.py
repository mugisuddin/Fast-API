from fastapi import FastAPI

app = FastAPI()

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


