from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from modules.database import Base


class Group(Base):
    __tablename__ = "GROUPS"

    id = Column(Integer, primary_key=True)
    group_number = Column(Integer)
    
    # Указывается имя класса, а не таблицы
    student = relationship('Student')


    def __init__(self, group_number: int):
        self.group_number = group_number
