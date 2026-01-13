# -*- coding: utf-8 -*-
from typing import Optional, List
from pydantic import BaseModel

class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate

class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes=True

class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True


class PerfilCreate(BaseModel):
    idade: int
    endereco: str