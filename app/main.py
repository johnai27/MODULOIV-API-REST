from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Students API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/students", response_model=list[schemas.StudentResponse])
def read_students(
    major: str = None,
    semester: int = None,
    is_active: bool = None,
    db: Session = Depends(get_db)
):
    return crud.get_students(db, major, semester, is_active)

@app.get("/api/students/{student_id}", response_model=schemas.StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id)

@app.post("/api/students", response_model=schemas.StudentResponse, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/api/students/{student_id}", response_model=schemas.StudentResponse)
def update_student_full(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.update_student(db, student_id, student.model_dump())

@app.patch("/api/students/{student_id}", response_model=schemas.StudentResponse)
def update_student_partial(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_student(db, student_id, student.model_dump(exclude_unset=True))

@app.delete("/api/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.soft_delete_student(db, student_id)
