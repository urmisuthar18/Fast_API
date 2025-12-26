from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title= "Item Management API",
    description= "API for managaing items",
    version="1.2.0"
)

# Define a Pydantic model for request/response
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# GET endpoint with parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str=None):
    return {"item_id": item_id, "q": q}

# POST endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# PUT endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}

# DELETE endpoint to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"measage": f"Item {item_id} deleted"}