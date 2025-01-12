from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

@app.get("/idomyself", tags=['Idomyselfs'])
async def get_idomyselfs() -> dict:
    return {"Data": idomyselfs}

@app.post("/idomyself", tags=["Idomyselfs"])
async def add_idomyself(idomyself: dict) -> dict:
    idomyselfs.append(idomyself)
    return {
        "data" : "A Idomyselfs is Added!"
    }
    
@app.put("/idomyself/{id}", tags=["Idomyselfs"])
async def update_idomyself(id: int, body: dict) -> dict:
    for idomyself in idomyselfs:
        if (int(idomyself["id"])) == id:
            idomyself["Activity"] = body["Activity"]
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"This Todo with id {id} is not found!"
    }

@app.delete("/idomyself/{id}", tags=["Idomyselfs"])
async def delete_idomyself(id: int) -> dict:
    for idomyself in idomyselfs:
        if int(idomyself["id"]) == id:
            idomyselfs.remove(idomyself)
            return {
                "data": f"Todo with id {id} has been deleted!"
            }
    return {
        "data": f"Todo with id {id} was not found!"
    }

idomyselfs = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]