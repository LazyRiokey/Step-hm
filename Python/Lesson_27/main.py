from faker import Faker

from modules.database import create_db, session
from modules.student import Student
from modules.groups import Group
from modules.lessons import Lesson


def create_database(load: bool = False):
    create_db()

    if load:
        load_fake_data(session())


def load_fake_data(session: session):

    group_1 = Group(group_number='2180')
    group_2 = Group(group_number='2181')
    group_3 = Group(group_number='2182')
    group_4 = Group(group_number='2183')

    session.add(group_1)
    session.add(group_2)
    session.add(group_3)
    session.add(group_4)

    session.commit()

    groups = [group_1, group_2, group_3, group_4]

    faker = Faker('ru-RU')

    for _ in range(100):
        full_name = faker.name().split(' ')
        age = faker.random.randint(18, 25)
        address = faker.address()
        group = faker.random.choice(groups)
        student = Student(full_name, age, address, id_group=group.id)
        session.add(student)

    session.commit()

    lessons_names = ['Автоматизированные системы управления', 'Автоматика', 'Вычислительная техника',
    'Защита информации', 'Системы сбора и обработки данных', 'Инженерная графика', 'Материаловедение в машиностроении',
    'Проектирования технологических машин', 'Технологии машиностроения', 'Химия и химическая технология',
    'Автоматизированные электротехнологические установки', 'Теоретические основ электротехники', 'Электромеханика',
    'Электропривода и автоматизация промышленных установок', 'Электротехнические комплексы', 'Алгебра и математическая логика',
    'Высшая математика', 'Вычислительные технологии', 'Инженерная математика', 'Параллельные вычислительные технологии',
    'Прикладная математика', 'Теоретическая и прикладная информатика']

    for l_name in lessons_names:
        lesson = Lesson(lesson_name=l_name)
        for gr_num in groups:
            lesson.groups.append(gr_num)
    
    session.commit()
    session.close()
