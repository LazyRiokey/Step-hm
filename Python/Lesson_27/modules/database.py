from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Навание БД
dbName = 'University.db'

# Подключение к БД
engine = create_engine(f'sqlite:///Lesson_26\database\{dbName}') 
# Запуск сессии для работы с БД
session = sessionmaker(bind=engine)

# Создание шаблона.
Base = declarative_base()

# Создание БД
def create_db():
    Base.metadata.create_all(engine)