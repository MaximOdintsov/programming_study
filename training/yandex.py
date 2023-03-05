# a = input()
# nums = a.split(' ')
# sum_ = 0
# for num in nums:
#     sum_ += int(num)
# print(sum_)

# with open('input.txt', 'r') as input_:
#     nums = input_.read()
#     nums = nums.split(' ')
#     sum_ = 0
#     for num in nums:
#         sum_ += int(float(num))
#
#     with open('output.txt', 'w') as output:
#         output.write(str(sum_))

# with open('input.txt', 'r') as text:
#     text = text.read()
#     items = text.split()
#     if len(items) == 2:
#         jewels = []
#         unique = set(items[0])
#         [jewels.append(item) for item in unique]
#         nums = 0
#         for jewel in jewels:
#             nums += items[1].count(jewel)
#
#         print(nums)
#     else:
#         print(0)

# Первая строка содержит одно целое число - количество клавиш на клавиатуре.
# Вторая строка содержит N целых чисел — идентификаторы символов на клавишах. Гарантируется, что все значения различны.
# Третья строка содержит N целых чисел. Число ri задает номер ряда на клавиатуре, в котором расположена клавиша с символом ci
# Четвертая строка содержит одно целое число — количество символов в реферате.
# Пятая строка содержит K целых чисел. — идентификаторы символов реферата в порядке набора на клавиатуре. Гарантируется, что для любого s j существует такой
# i, что sj = ci — любой символ из реферата присутствует на клавиатуре.

# try:
#     with open('input.txt', 'r') as text:
#         strings = text.read().splitlines()
#         strings = list(filter(None, strings))
#
#         if len(strings) == 5:
#             str1 = strings[0]  # Первая строка содержит одно целое число - количество клавиш на клавиатуре.
#             if int(str1) <= 0:
#                 raise ValueError
#
#             str2 = strings[1].split(' ')  # Вторая строка содержит N целых чисел — идентификаторы символов на клавишах.
#             str3 = strings[2].split(' ')  # Третья строка содержит N целых чисел. Число ri задает номер ряда на клавиатуре, в котором расположена клавиша с символом ci
#             if len(str2) != len(str3):
#                 raise ValueError
#             str4 = strings[3]  # Четвертая строка содержит одно целое число — количество символов в реферате.
#             if int(str4) < 1:
#                 raise ValueError
#             str5 = strings[4].split(' ')  # Пятая строка содержит K целых чисел. — идентификаторы символов реферата в порядке набора на клавиатуре.
#             if len(str5) < 1:
#                 raise ValueError
#
#             keys = {}
#             for i in range(int(str1)):
#                 keys[str2[i]] = str3[i]
#
#             num_transitions = 0
#             prev_row = str5[0]
#             for key in str5:
#                 curr_row = keys.get(key)
#                 if prev_row != curr_row:
#                     num_transitions += 1
#                 prev_row = curr_row
#
#             print(num_transitions)
#         else:
#             print(0)
# except ValueError:
#     print(0)


with open('input.txt', 'r') as text:
    strings = text.read().splitlines()
    strings = list(filter(None, strings))

    N, X, T = strings[0].split(' ')
    N, X, T = int(N), int(X), int(T)
    a = [int(string) for string in strings[1].split(' ')]

    sculptures = {i+1: a[i] for i in range(len(a))}
    sorted_sculptures = {}

    sorted_keys = sorted(sculptures, key=sculptures.get)
    for w in sorted_keys:
        sorted_sculptures[w] = sculptures[w]

    ideal_sculptures_list = []
    ideal_sculptures_nums = 0
    for sculpture in sorted_sculptures:
        value = sorted_sculptures.get(sculpture)
        if value == X:
            ideal_sculptures_list.append(sculpture)
            ideal_sculptures_nums += 1
        elif abs(X-value) <= T:
            ideal_sculptures_list.append(sculpture)
            ideal_sculptures_nums += 1
            T = T - (abs(X - value))

    print(ideal_sculptures_nums)
    print(*ideal_sculptures_list)