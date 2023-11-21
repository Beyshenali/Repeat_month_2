# Абстаркция

# class Transport:  # Абстрактный класс
#     def __init__(self, name, model, color, year):
#         self.name = name
#         self.model = model
#         self.color = color
#         self.year = year

#     def __str__(self):
#         return f"""название - {self.name}, 
# модель - {self.model}
# цвет - {self.color}
# год выпуска - {self.year}"""

# Наследование
# Инкапсуляция
# class Car(Transport):
#     def __init__(self, name, model, color, year):
#         Transport.__init__(self, name, model, color, year)
#         # super().__init__(name, model, color, year)
#         self.penalties = 0
#         self.odometer = 0
#         self.is_drive = False
#         self.__wheels = 4

#     @property
#     def wheels(self):
#         return self.__wheels

#     @wheels.setter
#     def wheels(self, new_wheels):
#         self.__wheels = new_wheels

#     def start_up(self):
#         self.is_drive = True
#         print("Машина от алды")
    
#     def drive(self, km, pen):
#         if self.is_drive:
#             self.odometer += km
#             self.penalties += pen
#         else:
#             print("Биринчи машинаны жургузунуз")
            


#     def __str__(self):
#         return super().__str__() + f"\nштрафы - {self.penalties}, \nкилометраж - {self.odometer}"
        

# mersedes = Car("G63", "s", "black", 2001)
# mersedes.start_up()
# mersedes.drive(10, 0)
# print(mersedes)
# print(mersedes.wheels)

# Полиморфизм

# class Toys:
#     def __init__(self):
#         pass

#     def play(self):
#         pass

# class Ball(Toys):
#     def play(self):
#         print("Мячик прыгает")

# class Doll(Toys):
#     def play(self):
#         print("Кукла поет")

# class Machine(Toys):
#     def play(self):
#         print("Машина едет")

# kukla = Doll()
# top = Ball()
# masina = Machine()

# kukla.play()
# masina.play()
# top.play()

# Декораторы
# def say_hello_in_third_language(f):
#     def algoritm():
#         print("Салам")
#         f()
#         print("Здравствуйте")
#     return algoritm

# @say_hello_in_third_language
# def say_hello_in_english():
#     print("Hello world")
# say_hello_in_english()