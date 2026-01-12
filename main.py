from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

models.base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudantes/", response_model=schemas.EstudanteResponse)

def create_student(
        student: schemas.EstudanteCreate,
        db: Session = Depends(get_db)):
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.post("/matriculas/", response_model=schemas.MatriculaResponse)

def create_disciplina(
        disciplina: schemas.MatriculaCreate,
        db: Session = Depends(get_db)):
    db_matricula = models.Matricula(**disciplina.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula
    

@app.get("/estudantes/", response_model=List[schemas.EstudanteResponse])

def read_students(db: Session = Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students

@app.get("/matriculas/", response_model=List[schemas.MatriculaResponse])

def read_matriculas(db: Session = Depends(get_db)):
    matriculas = db.query(models.Matricula).all()
    return matriculas
