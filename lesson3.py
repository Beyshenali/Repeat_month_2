# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"ФИО: {self.name}, возраст: {self.age} - магический метод"

#     def info_user_1(self):
#         print (f"ФИО: {self.name}, возраст: {self.age} - простой метод")

#     def info_user_2(self):
#         return (f"ФИО: {self.name}, возраст: {self.age} - простой метод 2")

# person = Person("Geeks", 3)
# print(person)
# person.info_user_1()
# print(person.info_user_2())

# # Множественно наследование
# class Mum: # Roditelskiy klass
#     home = "Dom"
# class Dad: # Roditelskiy klass
#     car = "Mashina"

# class Son(Mum,Dad): # Docherniy klass
#     name = "Nechego"

# son = Son()
# print(son.car)


# class Phone:
#     def call(self):
#         return "Я звоню маме "

# class Camera:
#     def take_photo(self):
#         return "ya fotkayu otsa"
    
# class SmartPhone(Phone, Camera):
#     def alll(self):
#         return "ya fotkayu i takje zvonyu"
# smartphone = SmartPhone()
# print(smartphone.call())
# print(smartphone.take_photo())
# print(smartphone.alll())

# class Animals:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass
# class Cat(Animals):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

#     def speak(self):
#         return f"{self.name} {self.color} meow"
    
# cat = Cat("Byityk", "Sary")
# print(cat.speak())