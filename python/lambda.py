double_l = lambda x: x * 2

print('lambda double:', double_l(2))


def double_d(x):
    return x * 2


print('def double:', double_d(2))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: x % 2 == 0, my_list))
print('filter:', new_list)

new_list = list(map(lambda x: x**2, my_list))
print('map:', new_list)

