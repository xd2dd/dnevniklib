from pydantic import BaseModel
 
class Mark(BaseModel):
    id: int
    value: int
    comment: str
    subject_name: str
    subject_id: int
    control_form_name: str
    weight: int
    created_at: str
    is_exam: bool


    def get_normal_date(self, date):
        return date.replace('T', ' ', 1)

    def __str__(self):
        return \
            f"оценка: {self.value} вес: {self.weight} дата: {self.get_normal_date(self.created_at)}, комментарий: {self.comment if self.comment != '' else 'Не добавлен' }"