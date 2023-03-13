# ГЕНЕРАТОРЫ И ИТЕРАТОРЫ

# Генератор - это итератор, который можно итерировать только 1 раз.

# Итератор - объект, который поддерживает функцию next()
# и помнит о том, какой элемент будет браться следующим.

# Итерируемый объект - объект, который предоставляет возможность
# обойти свои элементы поочередно. Может быть преобразован в итератор


# Итерируемый объект (не поддерживает next(), т.к. это не итератор)
my_list = [2, 4, 6, 1, 85]

# Теперь это итератор (поддерживает next() )
iterator = iter(my_list)

for elem in iterator:
    print(elem)

for elem in iterator:
    print(elem)
