from sqlalchemy import Column, Integer, String, ForeignKey
from modules.database import Base

class Student(Base):
    __tablename__ = "STUDENT"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    partonomic = Column(String)
    age = Column(Integer)
    address = Column(String)
    group = Column(Integer, ForeignKey("GROUPS.id"))

    def __init__(self, full_name: list[str], age: int, address: str, id_group: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.partonomic = full_name[2]
        self.age = age
        self.address = address
        self.group = id_group
    
    def __repr__(self):
        info: str = str({'Фамилия': self.surname, 'Имя': self.name, 'Отчество': self.partonomic, 'Возраст': self.age, 'Адрес': self.address, 'Группа': self.group})

        return info