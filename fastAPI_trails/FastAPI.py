# # myapp/
# # ├── database.py      # DB connection
# # ├── models.py        # SQLAlchemy models
# # ├── schemas.py       # Pydantic schemas
# # ├── crud.py          # DB operations
# # └── main.py          # FastAPI routes
# # database.py file 

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# # sqllite 
# sqlalchmey_database_url = "sqlite:///.test.db"
# engine = create_engine(sqlalchmey_database_url, connect_args={"check_same_thread": False})
# sessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)
# Base = declarative_base()
# # dependency injection 
# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# # model.py tables defination 
# from sqlalchemy import Column,Integer, String, Float
# # from database import Base  # this import file from other's

# class Item(Base):
#     __tablename__ = "items"
#     id = Column(Integer,primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, nullable=True)
#     Price = Column(Float)
# #schemas.py -pydantic models(request/response)
# from pydantic import BaseModel
# from typing import Optional
# class ItemBase(BaseModel):  # shared properties
#     name : str
#     description: Optional[str] = None
#     price : Float
# class ItemCreate(ItemBase): # used when creating
#     pass
# class ItemUpdate(BaseModel):  # used when updating 
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[str] = None
# class ItemResponse(ItemBase):
#     id: int
#     class Config:
#         from_attributes  = True  # lets pydanic reads sqlalchmey objects
# # curd.py  database operations
# from sqlalchemy.orm import Session
# # import models, schemas # this is from other file 
# def get_item(db:Session, item_id: int):
#     # return db.query(models.Item).filter(models.Item.id == item_id).first() #<-- if you use other file use this
#     return db.query(Item).filter(Item.id == item_id).first()

# def get_items(db:Session, skip: int= 0, limit: int = 100):
#     # return db.query(models.Item).offeset(skip).limit(limit).all
#     return db.query(Item).offset(skip).limit(limit).all()
# # def create_item(db:Session, item:schemas.ItemCreate):
# def create_item(db:Session, item:ItemCreate):
#     # db_item = models.Item(**item.dict())
#     db_item = Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# # def update_item(db:Session, item_id: int, item:schemas.ItemUpdate):
# def update_item(db:Session, item_id: int, item:ItemUpdate):
#     db_item = db.query(Item).filter(Item.id == item_id)
#     if not db_item:
#         None
#     update_data = item.dict(exclude_unset = True)
#     for key, value in update_data.items():
#         setattr(db_item, key, value)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# def delete_item(db: Session, item_id: int):
#     db_item = db.query(Item).filter(Item.id == item_id)
#     if not db_item:
#         return None
#     db.delete(db_item)
#     db.commit()
#     return db_item

# # main.py 
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# import models, schemas, crud
# from database import engine, get_db

# # Create tables
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Items CRUD API")


# # CREATE
# @app.post("/items/", response_model=schemas.ItemResponse, status_code=201)
# def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     return crud.create_item(db=db, item=item)


# # READ all
# @app.get("/items/", response_model=List[schemas.ItemResponse])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud.get_items(db, skip=skip, limit=limit)


# # READ one
# @app.get("/items/{item_id}", response_model=schemas.ItemResponse)
# def read_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = crud.get_item(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item


# # UPDATE
# @app.put("/items/{item_id}", response_model=schemas.ItemResponse)
# def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
#     db_item = crud.update_item(db, item_id=item_id, item=item)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item


# # DELETE
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = crud.delete_item(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"message": "Item deleted successfully"}


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional, List

# mcp creation 
from fastapi_mcp import FastApiMCP


# ---------------- DATABASE SETUP ----------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # only needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ---------------- SQLALCHEMY MODEL (DB Table) ----------------
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)


# Create the table in the database
Base.metadata.create_all(bind=engine)


# ---------------- PYDANTIC SCHEMAS (Request/Response shapes) ----------------
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        from_attributes = True   # use orm_mode = True if on Pydantic v1


# ---------------- DB SESSION DEPENDENCY ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- FASTAPI APP ----------------
app = FastAPI(title="Items CRUD API")


# CREATE
@app.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# READ all
@app.get("/items/", response_model=List[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Item).offset(skip).limit(limit).all()


# READ one
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# UPDATE
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Only update fields the user actually sent
    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}         

mcp = FastApiMCP(
    app,
    name="Items CRUD MCP",
    description="MCP server exposing Items CRUD operations",
)
mcp.mount()