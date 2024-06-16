from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base

class Variante(Base):
    __tablename__ = "Variante"

    id = Column(Integer, primary_key=True)
    Start = Column(Integer, index=True)
    End = Column(Integer, index=True)
    Chr = Column(Integer, index=True)
    MAF = Column(Numeric, index=True)
    Nombre = Column(String, index=True)
    Tipo = Column(String, index=True)
    AleloREF = Column(String, index=True)
    AleloALT = Column(String, index=True)
    Id_gen = Column(Integer, ForeignKey("Gen.ID_GEN"))
    synonyms = Column(String, index=True)

    genes = relationship("Gen", back_populates="mygene")

class Gen(Base):
    __tablename__ = "Gen"

    ID_GEN = Column(Integer, primary_key=True)
    start = Column(Integer, index=True)
    end = Column(Integer, index=True)
    loci = Column(Numeric, index=True)
    chr = Column(Integer, index=True)
    id_pathway = Column(Integer, ForeignKey("Pathway.ID_KEGG"))

    rutas = relationship("Pathway", back_populates="mypath")
    mygene = relationship("Variante", back_populates="genes")

class Pathway(Base):
    __tablename__ = "Pathway"

    ID_KEGG = Column(Integer, primary_key=True)
    entry = Column(String, index=True)
    pathway = Column(String, index=True)
    name = Column(String, index=True)
    ID_gen = Column(Integer, index=True)

    mypath = relationship("Gen", back_populates="rutas")
