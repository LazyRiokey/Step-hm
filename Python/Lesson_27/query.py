import os

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session as SQLSession
from modules.database import dbName, session
import main
from modules.groups import Group
from modules.student import Student
from modules.lessons import Lesson, association_table

if not os.path.exists(dbName):
    main.create_database(False)

session: SQLSession = session()

os.system('cls')


""" Запрос 1 """


# students = session.query(Student).filter(Student.age == 20).count()
# print(students)
# session.close()


""" Запрос 2 """


# students = session.query(Student).filter(Student.age == 20)

# for student in students:
#     print(student)

# session.close()


""" Запрос 3 """


# students = session.query(Student).filter(Student.age >= 20)

# for student in students:
#     print(student)

# session.close()


""" Запрос 4 """


# students = session.query(Student).filter(Student.age >= 20).count()
# print(students)

# session.close()


""" Запрос 5 """


# students = session.query(Student).filter(Student.age >= 20, and_(Student.surname.like('А%')))

# for student in students:
#     print(student)

# session.close()


""" Запрос 6 """


# students = session.query(Student).filter(Student.age >= 20, or_(Student.surname.like('А%')))

# for student in students:
#     print(student)

# session.close()


""" Запрос 7 """


# students = session.query(Student).join(Group).filter(Group.group_number == '2180')

# for student in students:
#     print(student)

# session.close()


""" Запрос 8 """


# students = session.query(Group.group_number, Lesson.lesson_name).filter(and_(
#     association_table.c.lesson_id == Lesson.id,
#     association_table.c.group_id == Group.id,
#     Group.group_number == 2180
# ))

# for student in students:
#     print(student)

# session.close()


""" Запрос 9 """


# students = session.query(Group.group_number, Lesson.lesson_name).filter(and_(
#     association_table.c.lesson_id == Lesson.id,
#     association_table.c.group_id == Group.id,
#     Group.group_number == 2182,
#     Lesson.lesson_name.like('В%')
# ))

# for student in students:
#     print(student)

# session.close()


""" Запрос 10 """


# student = session.query(Student).get(10)

# print(student)

# student.age = 16

# print(student)

# session.commit()
# session.close()


""" Запрос 11 """

# student = session.query(Student).filter(Student.age < 20)
# session.query(Student).filter(Student.age < 20).update({Student.age: Student.age + 1})

# for s in student:
#     print(s)

# session.commit()
# session.close()


""" Запрос 12 """


# student = session.query(Student).filter(Student.age == 16).one()

# print(student)

# session.delete(student)
# print(student)
# session.commit()
# session.close()


""" Запрос 13 """


# students = session.query(Student).filter(Student.surname.like('А%')).delete(synchronize_session='fetch')

# for s in students:
#     print(s)

# session.close()


""" Запрос 14 """


# students = session.query(Student).filter(Student.group == 3)
# session.query(Student).filter(Student.group == 1).update({Student.group: 3})

# for student in students:
#     print(student)


# session.close()


""" Запрос 15 """

try:
    session.query(Student).filter(Student.name.like('А%')).delete()

    session.commit()
except Exception:
    print("Что-то пошло не так")

    session.rollback()
finally:
    session.close()

session.close()

