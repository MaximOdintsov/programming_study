# Если a == b, то равен и hash
# Но равные хэши hash(a) == hash(b) не гарантируют равенство объектов
# Если хэши hash(a) != hash(b), то объекты точно не равны
# Хэш есть только у НЕИЗМЕНЯЕМЫХ объектов
# Ключом словаря может быть только хэшируемый неизменяемый тип данных,
# то есть, ключом словаря является не сам объект, а его хэш


a = 'python'
b = 'python'
print(hash(a), hash(b))

a = 34
print(hash(a))
a = 34.0
print(hash(a))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)
print('------------------------------------------------------------')
print(hash(p1), hash(p2), sep='\n')
print(p1 == p2)

d = {}
d[p1] = 1
d[p2] = 2
print(d)  # p1 и p2 для словаря являются разными объектами, тк их хэши не равны


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
print('------------------------------------------------------------')
print(hash(p1), hash(p2), sep='\n')
print(p1 == p2)

dct = {}
dct[p1] = 1
dct[p2] = 2
print(dct)  # p1 и p2 для словаря являются 1 и тем же объектом, тк их хэши равны