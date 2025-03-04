from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Student
from .schemas import StudentResponse

def get_all_students(db: Session):
    result = db.execute(select(Student.name))
    students = result.scalars().all()

    # Convert to a list of dictionaries matching StudentResponse schema
    return [{"name": student} for student in students]
