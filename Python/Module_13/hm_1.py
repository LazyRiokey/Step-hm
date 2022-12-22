# Задание 1
# Создайте класс Обувь. Необходимо хранить следующую информацию:
# - тип обуви;
#   ✓мужская,
#   ✓женская;
# - вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# - цвет;
# - цена;
# - производитель;
# - размер.
# Создайте необходимые методы для этого класса. Реа-
# лизуйте паттерн MVC для класса Обувь и код для исполь-
# зования модели, контроллера и представления.


from task_1 import colors, genders, shoes


class Model:
    def __init__(
        self,
        gender: str,
        type: str,
        color: str,
        price: float,
        manufacturer: str,
        size: int,
    ):
        self.gender = self.check_gender(gender)
        self.type = self.check_type(type)
        self.color = self.check_color(color)
        self.price = float(price)
        self.manufacturer = manufacturer
        self.size = size

    def get_enum(self, list):
        data = []
        for count, value in enumerate(list, start=1):
            data.append(f"{count}. {value}\n")
        return data

    def check_gender(self, gender):
        try:
            if gender in genders.GENDERS:
                return genders.GENDERS.get(gender)
            else:
                raise Exception
        except Exception:
            print("Gender must be 'M' - male or 'F' - female.")

    def check_type(self, type):
        try:
            if type in shoes.SHOES:
                return type
            else:
                raise Exception
        except Exception:
            print("Incorrect type of shoes. Please check this list:\n")
            print(self.get_enum(shoes.SHOES))

    def check_color(self, color):
        try:
            if color.capitalize() in colors.COLORS:
                return color
            else:
                raise Exception
        except Exception:
            print("Incorrect color. Please check this list:\n")
            print(self.get_enum(colors.COLORS))


class ModelView(Model):
    def __str__(self):
        return f"""
Gender: {self.gender},
Type: {self.type},
Color: {self.color},
Price: {self.price},
Manufacturer: {self.manufacturer},
Size: {self.size}."""


class Controller(ModelView):
    def set(self, var, value):
        try:
            var = var.lower()
            if var == "gender":
                self.gender = self.check_gender(value.title())
            elif var == "type":
                self.type = self.check_type(value.title())
            elif var == "color":
                self.color = self.check_color(value.title())
            elif var == "price":
                self.price = float(value)
            elif var == "manufacturer":
                self.manufacturer = value.title()
            elif var == "size":
                self.size = value
            else:
                raise TypeError
        except TypeError:
            print(f"Such a variable '{var}' does not exist!")


shoe_1 = Controller("M", "Ballet flats", "Black", 4500, "Any manufacturer", 39)
print(shoe_1)
shoe_1.set('gender', 'F')
print(shoe_1)
shoe_1.set('color', 'red')
print(shoe_1)



