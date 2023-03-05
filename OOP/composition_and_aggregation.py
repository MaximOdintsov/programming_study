from typing import List


class Engine:
    """Этот класс не может существовать без Car (композиция)"""
    def __init__(self, power: int):
        self.power = power

    def message(self):
        print(f'Двигатель с мощностью {self.power} л.с. запущен.')


class Wheel:
    """Этот класс не может существовать без Car (композиция)"""
    def __init__(self, diameter):
        self.diameter = diameter

    def message(self):
        print(f'Колесо с диметром {self.diameter} крутится.')


class Freshener:
    """Этот класс живет независимо от Car, может приниматься другими классами"""
    def __init__(self):
        print('Освежитель освежает пространство')


class Car:
    def __init__(self, name, freshener_):
        self.name = name
        
        # КОМПОЗИЦИЯ (классы создаются внутри Car, не могут создаваться извне)
        # Если удалить класс Car, то engine и wheels тоже удалятся
        self.engine = Engine(200)
        self.wheels = [Wheel(30) for _ in range(4)]

        # АГРЕГАЦИЯ (классы создаются извне, а в классе Car просто принимаются)
        # Если удалить класс Car, то freshener останется жить своей жизнью
        self.freshener = freshener_

    def parts_check(self):
        # ДЕЛЕГИРОВАНИЕ
        print(f'Автомобиль: {self.name}')
        parts = [self.engine, *self.wheels]  # * - распаковка списка

        for part in parts:
            part.message()


class Flat:
    def __init__(self, freshener_):
        self.freshener = freshener_


freshener = Freshener()

bmw = Car('bmw', freshener)
bmw.parts_check()

flat = Flat(freshener)