# Задание 2
# Создайте класс Рецепт. Необходимо хранить следующую информацию:
# - название рецепта;
# - автор рецепта;
# - тип рецепта (первое, второе блюдо и т.д.);
# - текстовое описание рецепта;
# - ссылка на видео с рецептом;
# - список ингредиентов;
# - название кухни (итальянская, французская, украинская и т.д.).
# Создайте необходимые методы для этого класса.
# Реализуйте паттерн MVC для класса Рецепт и код для
# использования модели, контроллера и представления.


class Model:
    def __init__(
        self,
        recipe: str,
        author: str,
        type: str,
        description: str,
        url: str,
        ingredients: dict,
        kitchen: str,
    ):
        self.recipe = self.check_on_str(recipe)
        self.author = self.check_on_str(author)
        self.type = self.check_on_str(type)
        self.description = self.check_on_str(description)
        self.url = self.check_on_str(url)
        self.ingredients = self.check_on_dict(ingredients)
        self.kitchen = self.check_on_str(kitchen)
    
    def check_on_str(self, value):
        try:
            if type(value) == str:
                return value
            else:
                raise TypeError
        except TypeError:
            print(f"The name of the variable should be a str!")
    
        
    def check_on_dict(self, value):
        try:
            if type(value) == dict:
                return value
            else:
                raise TypeError
        except TypeError:
            print(f"The name of the variable should be a dict!")


class ModelView(Model):
    def __str__(self):
        return f"""
Recipe: {self.recipe},
Author: {self.author},
Type: {self.type},
Description: {self.description},
URL: {self.url},
Ingredients: {self.ingredients},
Name of the kitchen: {self.kitchen}"""


class Controller(ModelView):
    def set(self, var, value):
        var = self.check_on_str(var.lower())

        try:
            if var == "recipe" and self.check_on_str(value) != None:
                self.recipe = value
            elif var == "author" and self.check_on_str(value) != None:
                self.author = value
            elif var == "type" and self.check_on_str(value) != None:
                self.type = value
            elif var == "description" and self.check_on_str(value) != None:
                self.description = value
            elif var == "url" and self.check_on_str(value) != None:
                self.url = value
            elif var == "ingredients" and self.check_on_dict(value) != None:
                self.ingredients = value
            elif var == "kitchen" and self.check_on_str(value) != None:
                self.kitchen = value
            else:
                raise TypeError
        except TypeError:
            print(f"Such a variable '{var}' does not exist!")

my_recipe = Controller(
    "Apple Pie",
    "Someone in internet",
    "Dessert",
    "Tasty apple pie for all family",
    "https://some_adress.com",
    {
        "Egg yolks": "2 piece",
        "Sugar": "140g",
        "Butter": "50g",
        "Milk": "125ml",
        "Flour": "180g",
        "Baking powder": "4g",
        "Salt": "3g",
        "Apple": "4 piece",
    },
    "Italian"
)

print(my_recipe)
my_recipe.set("ingredients", 1234)
print(my_recipe)