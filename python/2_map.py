lst = [1, 2, -3, 4, -5]
string_lst = ['python', 'map', 'objects']

# map - итератор
a = map(str, lst)

str_lst = list(a)
print(str_lst)

# вызывать саму функцию не нужно
new_lst = list(map(abs, lst))
print(new_lst)


# для map функция должна принимать только 1 значение
def f(x):
    return x**2


custom_lst = list(map(f, lst))
print(custom_lst)


len_lst = list(map(len, string_lst))
print(len_lst)


# также, map может принимать методы объектов
upper_lst = list(map(str.upper, string_lst))
print(upper_lst)


# map может принимать lambda-функции
lambda_lst = list(map(lambda x: x[::-1], string_lst))
print(lambda_lst)


# можно преобразовывать строки в списки
list_lst = list(map(list, string_lst))
sorted_lst = list(map(sorted, list_lst))
print(list_lst)
print(sorted_lst)


string = '0ff0ff0ff0'
num_lst = list(filter(lambda x: x % 3 != 0, range(len(string))))
new_string = ''.join(list(map(lambda x: string[x], num_lst)))
print(new_string)


lst = ['3r23432', 'erwerw', 'rewrw']
lst = list(map(lambda x: map(str, x), lst))
new_lst = [symbol for list_ in lst for symbol in list_]
print(new_lst)


# можно использовать при вводе нескольких значений в 1 строку
input_lst = list(map(int, input('Введите несколько чисел через пробел: ').split()))
print(input_lst)

