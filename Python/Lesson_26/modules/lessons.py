from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from modules.database import Base

# Связь многие ко многим
association_table = Table('association', Base.metadata,
                    Column('lesson_id', Integer, ForeignKey('LESSONS.id')),
                    Column('group_id', Integer, ForeignKey('GROUPS.id')))


class Lesson(Base):
    __tablename__ = "LESSONS"

    id = Column(Integer, primary_key=True)
    lesson_name = Column(String)
    groups = relationship('Group', secondary=association_table, backref='group_lesson')


    def __init__(self, lesson_name):
        self.lesson_name = lesson_name
