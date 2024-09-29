from pydantic import BaseModel

class Subject(BaseModel):
    id: int
    begin_time: str
    subject_name: str
    room_number: str