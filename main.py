from fastapi import FastAPI, HTTPException, status, Response

from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return db.get_sheep(id)


@app.get("/sheep", response_model=list[Sheep])
def read_all_sheep():
    return list(db.get_all_sheep().values())


@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    #Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    # Add the new sheep to the database
    db.data[sheep.id] = sheep
    return sheep # Return the newly added sheep data

@app.put("/sheep/{id}", response_model=Sheep, status_code=status.HTTP_200_OK)
def update_sheep(sheep: Sheep):
    if sheep.id not in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID doesn't exist")

    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID doesn't exist")
    del db.data[id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)