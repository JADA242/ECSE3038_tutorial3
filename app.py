from datetime import datetime
import uuid 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional 



app = FastAPI()

class Fruit(BaseModel):
    id: Optional[str] = None
    name: str
    variety: str
    quantity: int
    supplier: str
    harvest_date: datetime 
    creation_date: Optional[datetime] = None
    available: bool
    price: float
	
fruit_inventory = {}



@app.get("/api/fruits", response_model=List[Fruit])
def get_all_fruits():
    return [fruit for fruit in fruit_inventory.values() if fruit.available]



@app.get("/api/fruits/{fruit_id}", response_model=Fruit)
def get_fruit(fruit_id: str):
    fruit = fruit_inventory.get(fruit_id)
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit


@app.post("/api/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    fruit_id = str(uuid.uuid4())  
    fruit.id = fruit_id
    fruit.creation_date = datetime.now()  
    fruit_inventory[fruit_id] = fruit

    return fruit



@app.patch("/api/fruits/{fruit_id}", response_model=Fruit)
def update_fruit(
    fruit_id: str, 
    available: Optional[bool] = None, 
    price: Optional[float] = None, 
    quantity: Optional[int] = None
):
    fruit = fruit_inventory.get(fruit_id)
    if not fruit:

        raise HTTPException(status_code=404, detail="Fruit not found")

    if available is not None:
        fruit.available = available
    if price is not None:
        fruit.price = price
    if quantity is not None:
        fruit.quantity = quantity

    return fruit



@app.delete("/api/fruits/{fruit_id}")
def delete_fruit(fruit_id: str):
    fruit = fruit_inventory.get(fruit_id)
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not there")

    fruit.available = False  
    return {"message": f"Fruit '{fruit.name}' labelled as unavailable"}