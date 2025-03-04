from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import StudentResponse
from .crud import get_all_students

app = FastAPI()

@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return get_all_students(db)
