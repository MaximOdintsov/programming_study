# filter(function or None, iterable)
# Принимает только такие функции, которые возвращают True or False

num_lst = [10, 11, -1, 0, 34, 3, 402, 20, 112, -20, -20000, -10]
str_lst = ['python', 'map', 'objects', 'hello', 'goodbye', 'hi']
lst = [3, 401, 0, -3, '', 'hello', False, [], [23, 412], True, 30.12]
string = 'f3321f0fsI3Op1OI[24'
dct = {'MOSCOW': 900, 'SPB': 300, 'LA': 1000, 'PARIS': 400, 'NY': 1200}


def filter_(x):
    # if x > 10:
    #     return True
    # return False

    # возвращает True или False
    # return x > 10
    return x % 2 == 0


filter_lst = list(filter(filter_, num_lst))
print(filter_lst)

bool_lst = list(filter(bool, lst))
print(bool_lst)

lambda_lst = list(filter(lambda x: len(x) > 4, str_lst))
print(lambda_lst)

string_lst = list(filter(str.isdigit, string))
print(string_lst)

dct_lst = list(filter(lambda x: dct[x] > 700, dct))
print(dct_lst)

n = 25
lst = list(filter(lambda x: n % x == 0, range(1, n+1)))
print(lst)
