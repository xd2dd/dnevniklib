from pydantic import BaseModel


class Event(BaseModel):
    date: str
    description: str = None
    subject_name: str = None

    def __str__(self):
        return f'Дата: {self.date[:19]} Описание: {self.description}'