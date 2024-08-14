from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def calculate_sum(a: int, b: int):
    result = a + b
    return {"sum": result}






