from pydantic import BaseModel


class Homework(BaseModel):
    id: int
    description: str
    subject_id: int
    subject_name: str
    created_at: str
    is_done: bool = False

    def __str__(self):
        return f"{self.subject_name} {self.created_at}: {self.description} {'✅' if self.is_done else '❌'}"