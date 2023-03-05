print('_________________________________________________________________________________________')
# ПОЛИМОРФИЗМ ОПЕРАТОРОВ
print('!Polymorphism of the operators!\n')
num1 = 1
num2 = 2
str1 = "I'm learn "
str2 = "python"

print(num1 + num2)
print(str1 + str2)
print(str1 * num2)
print('_________________________________________________________________________________________')

# ПОЛИЗМОРФИЗМ ФУНКЦИЙ
print('!Function polymorphism!\n')

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

print('_________________________________________________________________________________________')

# ПОЛИМОРФИЗМ В МЕТОДАХ КЛАССА
print('!Polymorphism of class methods!\n')


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat = Cat("Fillip", 2.5)
dog = Dog("Sharik", 4)
animals = [dog, cat]

for animal in animals:
    animal.make_sound()  # нет класса-родителя, но оба могут вызывать одни и те же функции
    animal.info()

print('_________________________________________________________________________________________')

# ПОЛИМОРФИЗМ В ПЕРЕОПРЕДЕЛЕНИИ МЕТОДА
print('!Polymorphism in method redefinition!\n')

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


square = Square(4)
circle = Circle(7)
print(square)  # __str__
print(circle)  # __str__
print(circle.fact())
print(square.fact())
print(circle.area())
