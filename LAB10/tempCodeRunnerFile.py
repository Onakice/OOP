@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def read_root(name:str):
    return {"Hello": name}