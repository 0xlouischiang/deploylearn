from fastapi impot FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"result": "Welcome 2 FastAPI"}
