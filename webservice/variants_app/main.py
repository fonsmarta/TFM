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
		
@app.get("/variants/", response_model=list[schemas.Variante])
def read_variants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    variants = crud.get_variants(db, skip=skip, limit=limit)
    return variants

@app.get("/variant/{id}", response_model=schemas.Variante)
def read_variants(id: int, db: Session = Depends(get_db)):
    db_var = crud.get_variant(db, id=id)
    if db_var is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return db_var

#@app.get("/variant/{name}", response_model=schemas.Variant)
#def read_variants_by_name(nombre: String, db: Session = Depends(get_db)):
#    db_var_name = crud.get_variant_by_nombre(db, nombre=nombre)
#    if db_var_name is None:
#        raise HTTPException(status_code=404, detail="Variant not found")
#    return db_var_name
