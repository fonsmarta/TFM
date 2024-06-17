from sqlalchemy.orm import Session

from . import models, schemas

def get_variants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Variante).offset(skip).limit(limit).all()

def get_variant(db: Session, id: int):
    return db.query(models.Variante).filter(models.Variante.id == id).first()

def get_variant_by_nombre(db: Session, nombre: str):
    return db.query(models.Variante).filter(models.Variante.nombre == nombre).first()

def get_gen(db: Session, id_gen: int):
    return db.query(models.Gen).filter(models.Gen.id_gen == idgen).first()

def get_gen_by_nombre(db: Session, nombre: str):
    return db.query(models.Gen).filter(models.Gen.nombre == nombre).first()
