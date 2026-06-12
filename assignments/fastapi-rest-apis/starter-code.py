from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


app = FastAPI(title="FastAPI Assignment Starter")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    in_stock: bool = True


class Item(ItemCreate):
    id: int


# In-memory store for assignment practice.
items_db: dict[int, Item] = {}
next_item_id = 1


@app.get("/")
def root() -> dict[str, str]:
    # TODO: Return a welcome message.
    return {"message": "Welcome! Build your FastAPI endpoints here."}


@app.get("/health")
def health() -> dict[str, str]:
    # TODO: Return API status information.
    return {"status": "ok"}


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> Item:
    # TODO: Create and store a new item with an incrementing ID.
    global next_item_id
    item = Item(id=next_item_id, **payload.model_dump())
    items_db[item.id] = item
    next_item_id += 1
    return item


@app.get("/items", response_model=list[Item])
def list_items(
    min_price: float | None = Query(default=None, gt=0),
    in_stock_only: bool = False,
    limit: int = Query(default=50, ge=1, le=100),
) -> list[Item]:
    # TODO: Apply filters and limit values.
    values = list(items_db.values())

    if min_price is not None:
        values = [item for item in values if item.price >= min_price]

    if in_stock_only:
        values = [item for item in values if item.in_stock]

    return values[:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    updated = Item(id=item_id, **payload.model_dump())
    items_db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if item_id not in items_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del items_db[item_id]


# Run with: uvicorn starter-code:app --reload