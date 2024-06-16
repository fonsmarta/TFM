from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/variant/{id}", response_model=schemas.Variants)
def read_variants(id: int, db: Session = Depends(get_db)):
    db_var = crud.get_variant(db, id=id)
    if db_var is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return db_var

@app.get("/variant/{name}", response_model=schemas.Variants)
def read_variants_by_name(name: String, db: Session = Depends(get_db)):
    db_var_name = crud.get_variant_by_namedb, name=name)
    if db_var_name is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return db_var_name
