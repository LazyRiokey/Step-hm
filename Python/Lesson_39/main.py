class Model:
    
    def __init__(self, film_name: str, genre: str, year_of_issue: int, duration: int, studio: str, actors: dict):
        self.film_name = film_name
        self.genre = genre
        self.year_of_issue = year_of_issue
        self.duration = duration
        self.studio = studio
        self.first_name = actors.get('first_name')
        self.last_name = actors.get('last_name')
        self.role = actors.get('role') 


class ModelView(Model):
    def get(self):
        return f"""Название фильма: {self.film_name}, 
Жанр: {self.genre},
Длительность: {self.duration} мин.,
Название студии: {self.studio},
Актёр: Имя - {self.first_name},
Фамилия - {self.last_name},
Роль - {self.role}"""


class State(ModelView):
    def set(self, value):
        self.value = value


state = State()

print(state.get())
