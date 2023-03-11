# ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ (OCP)

# Сущности программы (классы, модули, функции и т.п.) должны быть открыты для расширения,
# но закрыты для изменений.

from abc import abstractmethod
from enum import Enum


# АНТИПАТТЕРН
class Products(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3


class DiscountCalculatorIncorrect:
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost

    def get_discount_price(self):
        """
        Чтобы добавить новую скидку на одежду или
        изменить скидку, нужно изменять базовый класс
        """
        if self.product_type == Products.SHIRT:
            print('Shirt:', self.cost * 0.95)
        elif self.product_type == Products.PANT:
            print('Pant:', self.cost * 0.80)
        elif self.product_type == Products.TSHIRT:
            print('Tshirt:', self.cost * 0.90)


shirt = DiscountCalculatorIncorrect(Products.SHIRT, 100)
tshirt = DiscountCalculatorIncorrect(Products.TSHIRT, 100)
pant = DiscountCalculatorIncorrect(Products.PANT, 100)

print('Incorrect Pattern')
for product in [shirt, tshirt, pant]:
    product.get_discount_price()


# ПАТТЕРН
class DiscountCalculatorCorrect:

    @abstractmethod
    def get_discount_price(self):
        pass


class DiscountCalculatorShirt(DiscountCalculatorCorrect):

    def __init__(self, cost):
        self.cost = cost

    def get_discount_price(self):
        print(f'Shirt: {self.cost * 0.95}')


class DiscountCalculatorTshirt(DiscountCalculatorCorrect):

    def __init__(self, cost):
        self.cost = cost

    def get_discount_price(self):
        print(f'Tshirt: {self.cost * 0.90}')


class DiscountCalculatorPant(DiscountCalculatorCorrect):

    def __init__(self, cost):
        self.cost = cost

    def get_discount_price(self):
        print(f'Pant: {self.cost * 0.80}')


shirt = DiscountCalculatorShirt(100)
tshirt = DiscountCalculatorTshirt(100)
pant = DiscountCalculatorPant(100)

print('Correct Pattern')
for product in [shirt, tshirt, pant]:
    product.get_discount_price()