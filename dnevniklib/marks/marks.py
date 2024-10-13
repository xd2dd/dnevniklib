from dnevniklib.student import Student
from requests import get
from dnevniklib.types import Mark

class Marks():
    def __init__(self, student: Student) -> None:
        self.student = student

    def get_marks_by_date(self, from_date, to_date):
        res = []
        response = get(
            f"https://school.mos.ru/api/family/web/v1/marks?student_id={self.student.id}&from={from_date}&to={to_date}",
            headers={
                "Auth-Token": self.student.token,
                "X-Mes-Subsystem": "familyweb"
            }
        )
        for mark in response.json()["payload"]:
            res.append(
                Mark(
                    id = mark["id"],
                    value = mark["value"],
                    comment = mark["comment"] if mark['comment'] is not None else "",
                    subject_name = mark["subject_name"],
                    subject_id = mark["subject_id"],
                    control_form_name = mark["control_form_name"],
                    weight = mark["weight"],
                    created_at = mark["created_at"],
                    is_exam = mark["is_exam"]
                )
            )
        return res