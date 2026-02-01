# Students Management API

REST API for managing university students information using FastAPI and SQLite.  
The system implements full CRUD operations, validations, and soft delete.

## Technologies Used

Python 3, FastAPI, SQLAlchemy, SQLite, Pydantic, Uvicorn.

## Project Structure

students_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
├── init_db.py
├── requirements.txt
├── README.md
├── .gitignore
└── students.db

## Installation, Execution and Testing

1. Clone the repository and enter the project directory.
```bash
git clone <repository-url>
cd students_api

## How to Run the Project

1. Open a terminal in the project root folder (where `requirements.txt` is located).

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

```md
## API Endpoints Examples

### Get all students
GET /api/students
Optional query parameters: major, semester, is_active
Example: GET /api/students?major=CS&semester=5

### Get student by ID
GET /api/students/{id}
Example: GET /api/students/1

### Create a new student
POST /api/students
Request body:
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@university.edu",
  "major": "Computer Science",
  "semester": 5,
  "gpa": 3.8,
  "enrollment_date": "2022-08-15"
}

### Update a student (full update)
PUT /api/students/{id}
Request body:
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@university.edu",
  "major": "Software Engineering",
  "semester": 6,
  "gpa": 3.9,
  "enrollment_date": "2022-08-15"
}

### Update a student (partial update)
PATCH /api/students/{id}
Request body:
{
  "semester": 7,
  "gpa": 3.6
}

### Delete a student (soft delete)
DELETE /api/students/{id}
This marks the student as inactive without removing the record.

## Use of AI

The following AI tool was used during development:

- **ChatGPT**  

Usage details:
- Generated the initial project structure
- Implemented CRUD endpoints with FastAPI
- Created database models and Pydantic schemas
- Assisted with validation rules and error handling
- Generated the database initialization script
- Helped writing documentation

All generated code was reviewed, adapted, and fully understood by the development team to comply with project requirements.