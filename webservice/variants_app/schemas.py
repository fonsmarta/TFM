from pydantic import BaseModel

# ----------- Variantes -----------------
class VarianteBase(BaseModel):
    Nombre: str
    Start: int
    End: int
    Chr: int
    MAF: float
    AleloREF: str
    AleloALT: str

class VarianteCreate(VarianteBase):
    pass

class Variante(VarianteBase):
    id: int

    class Config:
        orm_mode = True

# -------------- Genes -------------------
class GeneBase(BaseModel):
    ID_GEN: str

class GeneCreate(GeneBase):
    pass

class Gene(GeneBase):
    ID_GEN: int
    variants: list[Variante] = []

    class Config:
        orm_mode = True

# --------------- rutas --------------------
class PathwayBase(BaseModel):
    ID_KEGG: int

class PathwayCreate(PathwayBase):
    pass

class Pathway(PathwayBase):
    ID_KEGG: int
    Genes: list[Gene] = []

    class Config:
        orm_mode = True
