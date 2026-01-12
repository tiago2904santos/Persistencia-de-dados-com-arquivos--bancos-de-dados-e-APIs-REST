from sqlalchemy import \
    Column, Integer, String, ForeignKey
from database import base 

class Estudante(base):
    __tablename__ = "estudante"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    
    nome = Column(
        String(100),
        nullable=False
    )

    idade = Column(Integer)

class Matricula(base):
    __tablename__ = "Matriculas"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    estudante_id = Column(
        Integer,
        ForeignKey("estudante.id")
    )
    nome_disciplina = Column(
        String(100),
        nullable=False
    )