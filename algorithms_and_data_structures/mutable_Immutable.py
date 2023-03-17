# ИЗМЕНЯЕМЫЕ ТИПЫ
# list, dict, set
# НЕИЗМЕНЯЕМЫЕ ТИПЫ
# None, bool, int, float, str, tuple, frozenset


# РАБОТА НЕИЗМЕНЯЕМОСТИ
# x и y - одна и та же переменная с разными именами
x = "Python"
y = "Python"
print(type(x), type(y))
print(id(x), id(y))

x += '!'  # Удалили старую переменную и создали новую
print(type(x))
print(id(x))


# РАБОТА ИЗМЕНЯЕМОСТИ
lst = [2, 3, 5, 7]
print(type(lst))
print(id(lst))

lst.append(10)
print(id(lst))  # id не меняется, переменная та же самая, она не была пересоздана