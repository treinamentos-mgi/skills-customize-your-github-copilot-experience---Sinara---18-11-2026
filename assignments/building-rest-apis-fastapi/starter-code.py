from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Inventory API")

items = [
    {"id": 1, "name": "Notebook", "description": "A lined notebook"},
    {"id": 2, "name": "Pen", "description": "A blue ink pen"},
]

# TODO 1: Add GET / and GET /items routes.

# TODO 2: Add GET /items/{item_id}; return HTTP 404 when the item is missing.

# TODO 3: Define an ItemCreate Pydantic model and add POST /items.
