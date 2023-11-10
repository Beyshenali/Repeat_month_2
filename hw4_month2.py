# Задача 1
# Вам нужно создать программу для рисования различных геометрических фигур. 
# У вас должен быть базовый класс Shape (Фигура), а также несколько подклассов, 
# представляющих различные фигуры, такие как Circle (Круг) и Rectangle (Прямоугольник).
# Класс Shape должен иметь метод draw(), который будет выводить на экран "Рисуем фигуру". 
# Классы Circle и Rectangle должны наследовать этот метод и дополнительно реализовать свою функциональность. 
# Подсказка: Делайте точно так же как и на уроке

class Shape:
    def draw(self):
        print(f"Рисуем фигуру")

class Circle(Shape):
    def draw(self):
        print(f"Рисовал круглый фигура")

class Rectangle(Shape):
    def draw(self):
        print(f"Рисовал прямоугольный фигура")

shape = Shape()
shape.draw()

cir = Circle()
cir.draw()

rec = Rectangle()
rec.draw()


# Задача 2
# Создайте класс Counter (Счетчик), который будет представлять счетчик, 
# способный увеличиваться на заданное значение и возвращать текущее значение.
# Класс Counter должен иметь следующие методы:
# __init__(self): Конструктор для инициализации счетчика, начальное значение - 0.
# increment(self, value): Увеличивает счетчик на указанное значение.
# get_value(self): Возвращает текущее значение счетчика.

# 1-variant:
class Counter:
    def __init__(self):
      self.value = 0
    def increment(self,value):
        self.value +=value
    def get_value(self):
        return f"{self.value}"

counter = Counter()
print("Башталгыч счетчик")
print(counter.get_value())

counter.increment(5)
print("Учурдагы счетчик")
print(counter.get_value())

counter.increment(3)
print("жаныланган счетчик")
print(counter.get_value())

# 2-variant:

class Counter:
    def __init__(self):
        self.counter = 0
    
    def increment(self, value):
        self.counter += value
    
    def get_value(self):
        return f"текущее значение счетчика {self.counter}"

result = Counter()
result.increment(10)
print(result.get_value())
