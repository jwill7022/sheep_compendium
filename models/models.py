from typing import List

from pydantic import BaseModel


class Sheep(BaseModel):
    id: int
    name: str
    breed: str
    sex: str

def get_all_sheep(sheep: List[Sheep]):
    pass