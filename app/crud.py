from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app import models, schemas

def get_students(db: Session, major=None, semester=None, is_active=None):
    query = db.query(models.Student)

    if major:
        query = query.filter(models.Student.major == major)
    if semester:
        query = query.filter(models.Student.semester == semester)
    if is_active is not None:
        query = query.filter(models.Student.is_active == is_active)

    return query.all()

def get_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    try:
        db.commit()
        db.refresh(new_student)
        return new_student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already exists")

def update_student(db: Session, student_id: int, student_data: dict):
    student = get_student(db, student_id)

    for key, value in student_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student

def soft_delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    student.is_active = False
    db.commit()
