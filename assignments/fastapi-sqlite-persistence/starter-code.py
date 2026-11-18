import sqlite3
from contextlib import closing

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Persistent Inventory API")
DATABASE = "items.db"


class ItemCreate(BaseModel):
    name: str
    description: str


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL
                )
                """
            )


initialize_database()


@app.get("/items")
def list_items():
    # TODO: Query the database and return all items as dictionaries.
    raise NotImplementedError("Implement GET /items")


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Query by ID and raise HTTPException with status 404 if missing.
    raise NotImplementedError("Implement GET /items/{item_id}")


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    # TODO: Insert using SQL parameters and return the saved item.
    raise NotImplementedError("Implement POST /items")
