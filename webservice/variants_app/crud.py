from sqlalchemy.orm import Session

from . import models, schemas

def get_variant(db: Session, id: int):
    return db.query(models.Variant).filter(models.Variant.id == id).first()

def get_variant_by_nombre(db: Session, nombre: str):
    return db.query(models.Variant).filter(models.Variant.nombre == nombre).first()

def get_gen(db: Session, id_gen: int):
    return db.query(models.Genes).filter(models.Genees.id_gen == idgen).first()

def get_gen_by_nombre(db: Session, nombre: str):
    return db.query(models.Genes).filter(models.Genes.nombre == nombre).first()
