from dnevniklib import Student, Marks, Homeworks
from dnevniklib.notification.notification import Notification
from dnevniklib.notification.notification_wrap import NotificationWrap
from dnevniklib.schedule.schedule import Schedule
from dnevniklib.utils import Utils
from dnevniklib.marks.marks_wrap import MarksWrap
TOKEN = \
    "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMDI2MDk3Iiwic2NwIjoib3BlbmlkIHByb2ZpbGUiLCJtc2giOiJjNDQyODQyMS1mYjY2LTQwYWYtODYwYy0zZDI4YTRjNWY4NzQiLCJpc3MiOiJodHRwczpcL1wvc2Nob29sLm1vcy5ydSIsInJvbCI6IiIsInNzbyI6IjY4ZmM4NmJlLTNjMDYtNGUzZi04ZWJjLTY4NTRlMWMxMDE5YyIsImF1ZCI6IjQ6MSIsIm5iZiI6MTcyOTI2OTk4MCwiYXRoIjoic3VkaXIiLCJybHMiOiJ7MTpbMjA6MjpbXSwzMDo0OltdLDQwOjE6W10sMTgzOjE2OltdLDIxMToxOTpbXSw1MjU6NDQ6W10sNTMzOjQ4OltdXX0iLCJleHAiOjE3MzAxMzM5ODAsImlhdCI6MTcyOTI2OTk4MCwianRpIjoiNThmM2M5YzktMDJhNi00M2VmLWIzYzktYzkwMmE2YTNlZmY0In0.hxLGbJ8Mc_esAZ6n1Uju7vS8KYWpAXbCX9FXQ9Vt78WM37a2L8V4K2s9V8ACGwItiKGXnCP82Jxl4rMJMPMptflQ3A4V94ulSxiysq8SX6s8kgKcvYyeeR3ogjUK5ftX7dpx5L753XiKPiubmP4RRHF6QGZlgBrG97ORUGDdBdU5Fqpl5GJl0Em8yfnB-BIq9ZEUDzUI-G9qyCDV0D28rPBoRZw7oer5dx61tP5hFOwz0HKCFyffp1MJMq9c5oMll0VoWtikwRrMjzs8-ptN7Zk_2rp2nGc05k3qb3tzx7xIj9W2cIR9YmeokP4RXT98MkOs98pgNCc_aRT_FU1kmQ"
student = Student(TOKEN)

dateFrom = Utils.get_normal_date(2024, 9, 1)
dateTo = Utils.get_normal_date(2024, 10, 14)
# lstMark = marks.get_marks_by_date(dateFrom, dateTo)
# lstHomeWorks = Homeworks(student).get_homework_by_date(dateTo)
# print(len(lstHomeWorks))
# for homeWork in lstHomeWorks:
#     print(f"{homeWork.subject_name}: {homeWork.description}")
#
# for mark in lstMark:
#     print(f"{mark.subject_name}: {mark.value}")

schedule = Schedule(student)
home_work = Homeworks(student)
# for home_work in res:
#     print(home_work)



notify = Notification(student)
res = notify.get_marks_by_date()

print(NotificationWrap.build(res))