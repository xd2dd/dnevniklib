from aiogram.loggers import event

from dnevniklib import Student

from requests import get

from dnevniklib.types.event import Event


class Notification:

    def __init__(self, student: Student) -> None:
        self.student = student

    def get_marks_by_date(self):
        res = []

        responce = get(f"https://school.mos.ru/api/family/mobile/v1/notifications/search?student_id={self.student.id}",
                       headers={
                           'Auth-Token': self.student.token,
                           'Profile-Id': str(self.student.id),
                           "x-mes-subsystem": "familymp"
                       })

        for event in responce.json():
            if event['event_type'] == 'create_homework' or event['event_type'] == 'update_homework':
                res.append(
                    Event(
                        date=event['created_at'],
                        subject_name=event['subject_name'],
                        description=event['new_hw_description'],
                    )
                )
            elif event['event_type'] == 'create_mark' or event['event_type'] == 'update_mark':
                res.append(
                    Event(
                        date=event['created_at'],
                        subject_name=event['subject_name'],
                        description= 'Новая оценка: ' + event['new_mark_value'],
                    )
                )
            elif event['event_type'] == 'create_mark_comment' or event['event_type'] == 'update_mark_comment':
                res.append(
                    Event(
                        date=event['created_at'],
                        subject_name=event['subject_name'],
                        description='Обновлена оценка: ' + event['new_mark_value'],
                    )
                )
            elif event['event_type'] == 'delete_mark':
                res.append(
                    Event(
                        date=event['deleted_at'],
                        subject_name=event['subject_name'],
                        description='Удалена оценка: ' + event['old_mark_value'],
                    )
                )


        return res
