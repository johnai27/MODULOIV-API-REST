from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    major: str
    semester: int = Field(ge=1, le=12)
    gpa: Optional[float] = Field(ge=0.0, le=4.0)
    enrollment_date: date

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    major: Optional[str]
    semester: Optional[int] = Field(ge=1, le=12)
    gpa: Optional[float] = Field(ge=0.0, le=4.0)
    enrollment_date: Optional[date]
    is_active: Optional[bool]

class StudentResponse(StudentBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
