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
