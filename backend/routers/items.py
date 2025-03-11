from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.DB import schemas,crud,base

router = APIRouter()

@router.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_items(db, skip=skip, limit=limit)

@router.delete("/items/{item_id}", response_model=schemas.ItemResponse)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    item = crud.delete_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
