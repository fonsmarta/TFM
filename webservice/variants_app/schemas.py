from pydantic import BaseModel

# ----------- Variantes -----------------
class VariantBase(BaseModel):
    nombre: str

class VariantCreate(VariantBase):
    pass

class Variant(VariantBase):
    id: int
    id_gen: int

    class Config:
        orm_mode = True

# -------------- Genes -------------------
class GeneBase(BaseModel):
    nombre: str

class GeneCreate(GeneBase):
    pass

class Gene(GeneBase):
    ID_GEN: int
    variants: list[Variant] = []

    class Config:
        orm_mode = True

# --------------- rutas --------------------
class PathwayBase(BaseModel):
    email: str

class PathwayCreate(PathwayBase):
    pass

class Pathway(PathwayBase):
    ID_KEGG: int
    Genes: list[Gene] = []

    class Config:
        orm_mode = True
