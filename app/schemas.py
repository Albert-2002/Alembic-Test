from pydantic import BaseModel

class StudentResponse(BaseModel):
    name: str
