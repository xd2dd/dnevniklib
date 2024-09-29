from pydantic import BaseModel

class ScheduleEntity(BaseModel):
    id: int
    date: str
    subject_list: list

    def __str__(self):
        res = ''
        for item in self.subject_list:
            res = res +'\n' + item.subject_name + ' ' + item.begin_time + ' ' + item.room_number
        return res







