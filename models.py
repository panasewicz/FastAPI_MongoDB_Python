from pydantic import BaseModel

class students(BaseModel):
    name: str
    lastname: str

class message(BaseModel):
    message: str
    name: str
    lastname: str
    studentId: str

