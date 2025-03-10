from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    # name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    roll_no = Column(Integer, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)

    def __repr__(self):
        return f"<Student(name={self.name})>"