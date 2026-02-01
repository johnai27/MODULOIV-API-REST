from app.database import SessionLocal
from app.models import Student
from datetime import date

db = SessionLocal()

students = [
    Student(first_name="John", last_name="Doe", email="john@uni.edu", major="CS", semester=5, gpa=3.8, enrollment_date=date(2022,8,15)),
    Student(first_name="Jane", last_name="Smith", email="jane@uni.edu", major="Math", semester=3, gpa=3.5, enrollment_date=date(2023,1,10)),
    Student(first_name="Carlos", last_name="Perez", email="carlos@uni.edu", major="Engineering", semester=7, gpa=3.2, enrollment_date=date(2021,3,20)),
]

db.add_all(students)
db.commit()
db.close()
